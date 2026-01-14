"""
GPU memory clean up optimized to prevent OOM
"""

import gc
import torch
import numpy as np
import torch.nn.functional as F

def arctan_dihedral(sin: torch.tensor, cos: torch.tensor) -> torch.tensor:
    """ Conversion of arctan to dihedral angles  """
    result = torch.where(cos >= 0, torch.arctan(sin / cos),
                         torch.arctan(sin / cos) + np.pi)
    result = torch.where((sin <= 0) & (cos <= 0), result - np.pi * 2, result)

    return result * 180 / np.pi

class PredictNSP3():
    def __init__(self, model, transform, device):
        self.model = model
        self.transform = transform()
        self.device = device

        self.model = self.model.to(device)

    def inference(self, x, mask):
        """ Transforming and forwarding data to model """

        x = self.transform(x)
        # FIX: Wrap in torch.no_grad() to prevent gradient tracking
        with torch.no_grad():
            x = self.model(x.to(self.device), mask)
        return x

    def postprocessing(self, x):
        """ Processing of the ouput from the model """

        # FIX: Wrap in torch.no_grad() to prevent gradient tracking during postprocessing
        with torch.no_grad():
            # convert phi and psi radians to angles
            for i in range(x[0].shape[0]):
                x[0][i] = F.softmax(x[0][i], dim=1)
                x[1][i] = F.softmax(x[1][i], dim=1)
                x[2][i] = F.softmax(x[2][i], dim=1)
                
                x[4][i, :, 0] = arctan_dihedral(x[4][i][:, 0], x[4][i][:, 1])
                x[5][i, :, 0] = arctan_dihedral(x[5][i][:, 0], x[5][i][:, 1])

            x[4] = x[4][:, :, 0].unsqueeze(2)
            x[5] = x[5][:, :, 0].unsqueeze(2)

        return x

    def __call__(self, fasta):
        """ Prediction call logic """
        mask = [len(x[1]) for x in fasta]
        
        # FIX: Ensure entire prediction pipeline is in no_grad mode
        with torch.no_grad():
            x = self.inference(fasta, mask)
            x = self.postprocessing(x)

            identifier = [element[0] for element in fasta]
            sequence = [element[1] for element in fasta]
            
            # FIX: Convert to numpy and explicitly delete tensors
            prediction = []
            for i in range(len(x)):
                # Detach, move to CPU, convert to numpy
                pred_np = x[i].detach().cpu().numpy()
                prediction.append(pred_np)
            
            # FIX: Explicitly delete the tensor list to free GPU memory
            del x
        
        # FIX: Force garbage collection and clear CUDA cache
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

        return identifier, sequence, prediction
