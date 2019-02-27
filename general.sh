#!/bin/sh
cd oasc-master/oasc/
python run_$1.py $2
echo "\n train eseguito $1 $2\n"
python result.py $2 $1
echo "risultati\n\n"
cd ../../kit
python stats.py ../oasc-master/results/$1/$2.json
cd ../
#mplayer bell.mp3
