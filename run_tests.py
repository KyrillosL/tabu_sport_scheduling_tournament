import tabu
import time
import recuit
import numpy as np





#list_size=[6,8,10,12]#,14,16,18]
list_size=[10]
num_pass = 1
all_result={}
max_iteration=1000000

for x in list_size:
    print("nombre équipes ", x)
    list_mean = []
    for i in range(num_pass):

        start_time = time.time()
        #has_finished,_ =tabu.tabu(x, max_iteration)
        has_finished,_ =recuit.recuit_simule(x, max_iteration)
        if (has_finished):
            elapsed_time = time.time() - start_time
            list_mean.append(elapsed_time)
        print(list_mean)
    all_result[x]=np.mean(list_mean)
    print(all_result)
print("END")
print(all_result)
print("END")