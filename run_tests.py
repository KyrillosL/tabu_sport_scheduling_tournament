import tabu
import time
import recuit
import hill_climbing
import random_walk
import numpy as np


#h = Hill Climbing
#t = Tabu
#r = Recuit
#rw= random walk
method = 't'


max_iteration=1000000
#equipes=[6, 8, 10, 12]#,14,16,18]
equipes=[6]
num_pass = 1
all_result={}

for x in equipes:
    print("nombre équipes ", x)
    list_mean = []
    for i in range(num_pass):

        start_time = time.time()

        if method == 't':
            has_finished,_ =tabu.tabu(x, max_iteration)
        elif method == 'r':
            has_finished,_ =recuit.recuit_simule(x, max_iteration)
        elif method== 'h':
            has_finished, _ = hill_climbing.hill_climbing(x, max_iteration)
        elif method== 'rw':
            has_finished, _ = random_walk.ranomd_walk(x, max_iteration)

        if (has_finished):
            elapsed_time = time.time() - start_time
            list_mean.append(elapsed_time)
        print(list_mean)
    if len(list_mean)>0:
        all_result[x]=np.mean(list_mean)
    print(all_result)
print("END")
print(all_result)
