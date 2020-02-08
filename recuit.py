import tabu
import random
import math
import sys

import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt


number_of_teams= 14
max_score = (number_of_teams/2)*(number_of_teams-1)


def temperature(k, kmax):
    r = (1-(k/kmax))*10

    return r

def proba(delta):
    try:
        result = math.exp(delta)
    except OverflowError:
        print("OVERFLOW ERROR")
        result = float('inf')

    return  result

def recuit_simule(tournament):

    tournament.initial_configuration()
    best_eval = tournament.evaluate(tournament.list_match)/max_score
    current_configuration = tournament.list_match
    best_configuration = tournament.list_match
    best_eval_so_far = best_eval
    k=1
    kmax=100000
    score=[]
    time=[]
    time_not_ameliored=0
    while k<kmax and best_eval >0:


        if best_eval_so_far==0:
            print("Solution found: ", best_configuration)
            break
        #input()
        #neighborhood = current_configuration.neighborhood()
        #bc = tournament.get_best_config_from_neighborhood(neighborhood)

        tournament.arbitrary_neighborhood()
        current_eval = tournament.evaluate(tournament.list_match)/max_score

        energie = (current_eval + (current_eval-best_eval)/4)*2
        #energie =  ((current_eval/5) + (abs(current_eval-best_eval)/5)) # /(number_of_teams/6) CELLE CI ETAIT OK.
        #energie = abs(current_eval-best_eval_so_far) / 5 + (abs(current_eval - best_eval) / 5)
        temp = temperature(k,kmax)
        delta =  -energie /(temp*0.25)
        #delta = -2/temp
        prob = proba(delta)
        rnd = random.random()



        assigning = False
        if current_eval<=best_eval or (prob >rnd and time_not_ameliored>max_score) :
            assigning=True
            time_not_ameliored=0
        else:
            time_not_ameliored+=1



        if k%10000==0:
            out = "Ite " + str(k) + " Best Eval " + "{:.2f}".format(best_eval) + " Current " + "{:.2f}".format(current_eval) + " Prob " + "{:.2f}".format(prob) + " Rnd " + "{:.2f}".format(rnd) + \
                  " En " + "{:.2f}".format(energie) + " Tmp " + "{:.2f}".format(temp) + " Delta " + "{:.2f}".format(delta) + " Assigning " + str(assigning) + " Best so far "+str(best_eval_so_far)
            sys.stdout.write('\r'+out)
            sys.stdout.flush()

        if assigning :

            best_eval= current_eval
            best_configuration = current_configuration
            if best_eval <= best_eval_so_far:

                #print(out)
                best_eval_so_far=best_eval
        k+=1
        score.append(best_eval)
        time.append(k)
        #input()

    print("\nBEST EVAL SO FAR : ", best_eval_so_far, " Configuration: ", best_configuration)
    plt.plot(time,score,linestyle='solid', linewidth=0.5)
    #plt.scatter(time, score, s=0.01)  # ,  linestyle='solid', linewidth=1)
    plt.show()

    return best_configuration


tournament = tabu.Tournament(number_of_teams)
if tournament:
    recuit_simule(tournament)

