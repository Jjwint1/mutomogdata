#!/bin/sh

cd 1GeVvariance
python3 unconstrained_var.py
cd ../

cd 4GeVvariance
python3 unconstrained_var.py
cd ../

cd 20GeVvariance
python3 unconstrained_var.py
cd ../

cd 100GeVvariance
python3 unconstrained_var.py
cd ../

cd 500GeVvariance
python3 unconstrained_var.py
cd ../

