#!/bin/sh
cd oasc-master/oasc/
python run_randk.py Caren
echo "train eseguito\n\n"
python result.py Caren randk
echo "risultati\n\n"
cd ../../kit
python stats.py ../oasc-master/results/randk/Caren.json

