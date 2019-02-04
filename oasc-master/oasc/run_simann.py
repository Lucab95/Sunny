#! /usr/bin/env python

'''
python run_fkvar.py <SCENARIO_NAME>


comments
========
coordinate macro training process

Author: hearntest
'''

import os
import sys
import datetime
import time
from simann import *




def learn_scenario(param_learn):
  scenario_path,scenario_cv,scenario_outcome_dir,tdir,src_path,kRange,lim_nfeat,shouldWrappeFeature = parse_param_learn(param_learn)
  #shouldWrappeFeature==True

  start_time_fold = time.time()

  sub_scenario_path = scenario_cv

  print 'Building context ...'

  context = build_context(sub_scenario_path)

  # create resumable state
  #crea i file log_hard e log small
  log_file_hard,log_file_small,outcome_file = initFiles(scenario_outcome_dir,kRange[0],kRange[-1])

  #carica le feature dal file kb.args
  features = informative_feat(sub_scenario_path+'/'+tdir) if shouldWrappeFeature else ['']
  log_hard(log_file_hard,features)


  param_learn_fold = {
    'sub_scenario_path':sub_scenario_path,
    'log_file_hard':log_file_hard,
    'log_file_small':log_file_small,
    'outcome_file':outcome_file,
    'features':features
  }

  best_feats,best_k,par10f = learn_scenario_fold(param_learn,param_learn_fold,context,3)
  #best_feats,best_k,par10f = learn_scenario_fold(percorso e cartelle,log e features,context,3)

  #print 'Final result:',par10f, best_k, best_feats
  
  appendToFile(outcome_file,'train_1_b'+'; k='+str(best_k)+'; feats='+best_feats+'; par10='+str(par10f)+"\n\n")


#=======================================================
#=======================================================
#=======================================================

def main(args):
  if len(args) == 0:
    sys.exit('Missing Arg, E.g. Scenario Name ...')

  scenario_name = args[0]

  # configuration settings
  lim_nfeat = 5
  tdir = 't'
  outcomeDirname = 'outcome-simann'

  low_k = 3
  high_k = 30
  kRange = range(low_k,high_k) #imposto il range da 3 a 30 per ridurre il tempo di training
  
  # less insts make training faster
  # -1 means smart split that takes all the dataset, other integer means taking that amount of insts
  scenario_path,scenario_cv,src_path = prepare_scenario(scenario_name,tdir,1500)
  #crea tutta la cartella e sistemata tutto, decidendo se va splittato o no

  param_learn = {
  'scenario_path':scenario_path,
  'scenario_cv':scenario_cv,
  'scenario_outcome_dir':scenario_path+"/"+outcomeDirname,
  'tdir':tdir,
  'src_path':src_path,
  'kRange':kRange,
  'lim_nfeat':lim_nfeat,
  'shouldWrappeFeature':True
  }
  learn_scenario(param_learn)



if __name__ == '__main__':
  main(sys.argv[1:])
  
