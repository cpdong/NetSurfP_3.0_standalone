# NetSurfP 3.0 minimal version

**Disclaimer**
´´´
This repository is a fork of NetSurfP-3.0 provided solely for demonstration and installation convenience. Users must obtain the official NetSurfP-3.0 package, license, and model weights directly from the official website: https://services.healthtech.dtu.dk/services/NetSurfP-3.0/.

No model weights or licensed materials are distributed in this repository. This fork should not be considered an official distribution and is intended only to facilitate quick testing and GitHub-based installation workflows.
´´´

**Getting started**

´´´
# Setup environment
conda env create --file environment.yml
conda activate nsp3
python setup.py install
pip3 install -r requirements.txt

# Run example FASTA
python nsp3.py -m models/nsp3.pth -i example.fasta -o test
´´´

Only amino acid input is accepted, maximum (5000) sequences or a total of (10M) residues, or set in nsp3/config.yml. Moreover, the application stops if there are incorrect residue letters in the fasta file.

**Configuration**

The maximum sequences and total residues can be modified on the nsp3/config.py file.
