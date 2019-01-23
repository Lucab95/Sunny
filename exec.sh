#!/bin/sh
cd oasc-master/oasc/
python run_fkvarRand.py Caren
echo "train eseguito\n\n"
python result.py Caren fkvar
echo "risultati\n\n"
cd ../../kit
python stats.py ../oasc-master/results/fkvar/Caren.json

