#!/bin/sh
cd oasc-master/oasc/
python run_simann.py Svea
echo "train eseguito\n\n"
python result.py Svea simann
echo "risultati\n\n"
cd ../../kit
python stats.py ../oasc-master/results/simann/Svea.json

