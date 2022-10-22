# ChemDesc

Parallel computation of descriptors for molecular chemistry.

## Installation

This library is meant to be used by [BBOMol](https://github.com/jules-leguy/BBOMol) or 
[XAIMol](https://github.com/jules-leguy/XAIMol). Thus, it is assumed here than one of these libraries is already 
installed and that the *evomolenv* environment is already set up. To install ChemDesc, type the following commands
in the shell.

```shell script
$ cd path/to/chemdesc/installation                        # Go to the directory in which you want chemdesc to be installed
$ git clone https://github.com/jules-leguy/ChemDesc.git   # Clone ChemDesc
$ cd ChemDesc                                             # Move into ChemDesc directory
$ conda activate evomolenv                                # Activate environment
$ conda install -c conda-forge dscribe==1.2.1             # Installing DScribe dependency
$ python -m pip install .                                 # Install ChemDesc
```