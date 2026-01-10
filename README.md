# NetSurfP 3.0 standalone version

# Disclaimer
This repository is an unofficial fork of NetSurfP-3.0 and is provided solely for demonstration and installation convenience. Users must obtain the official NetSurfP-3.0 package, license, and model weights directly from the official website:
https://services.healthtech.dtu.dk/services/NetSurfP-3.0/

No model weights or licensed materials are distributed in this repository. This fork should not be considered an official distribution and is intended only to facilitate quick testing and GitHub-based installation workflows. Without a valid NetSurfP-3.0 license, users will not have access to the full functionality of NetSurfP-3.0 or be able to perform any predictions.

The official GitHub repository for NetSurfP-3.0 is: https://github.com/Eryk96/NetSurfP-3.0

All intellectual property rights, credit, and acknowledgments belong to the original authors and the Technical University of Denmark (DTU). Users should cite the original publication: Høie, M. H., et al. NetSurfP-3.0: accurate and fast prediction of protein structural features by protein language models and deep learning. Nucleic Acids Research, 50(W1), W510–W515 (2022).


# **Getting started**

´´´
## Setup environment
conda env create --file environment.yml
conda activate nsp3
python setup.py install
pip3 install -r requirements.txt

## Run example FASTA
python nsp3.py -m models/nsp3.pth -i example.fasta -o test

´´´

Only amino acid input is accepted, maximum (5000) sequences or a total of (10M) residues, or set in nsp3/config.yml. Moreover, the application stops if there are incorrect residue letters in the fasta file.

**Configuration**

The maximum sequences and total residues can be modified on the nsp3/config.py file.


Users must obtain the official NetSurfP-3.0 license, and model weights from the official website: https://services.healthtech.dtu.dk/services/NetSurfP-3.0/.
