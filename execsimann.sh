#!/bin/sh
cd oasc-master/oasc/
python run_simann.py Caren
echo "train eseguito\n\n"
python result.py Caren simann
echo "risultati\n\n"
cd ../../kit
python stats.py ../oasc-master/results/simann/Caren.json

