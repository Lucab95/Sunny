#! /usr/bin/env python

'''

python stats.py ../path/result.json


comments
========
Wrapper to use original OASC result evaluation

Author: HearNest

'''

import os
import csv
import sys
from subprocess import Popen


def main(args):
  if len(args) == 0:
    sys.exit('Missing Arg, E.g. python stats.py [file path in json, e.g. ../Bado.json]')

  jsonpath = args[0]

  if not os.path.exists(jsonpath):
    print 'File not found',jsonpath
    sys.exit()

  filename = jsonpath.split("/")[-1]
  scenario =  filename.split(".")[0]


  root_arr = os.path.realpath(__file__).split('/')[:-1]
  root = '/'.join(root_arr) 
  script = root+'/validation/validate_cli.py'

  test_folder = root+'/data/oasc_test_data/'+scenario+'/'
  train_folder = root+'/data/oasc_scenarios/train/'+scenario+'/'

  cmd = 'python3 ' + script + ' --result_fn ' + jsonpath +' --test_as '+ test_folder + ' --train_as  ' + train_folder
  # print cmd
  proc = Popen(cmd.split())
  proc.communicate()


if __name__ == '__main__':
  main(sys.argv[1:])
  