import model_sts
import random
import math
import sys

import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt





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

def recuit_simule(size =6, max_iteration=10000):
    number_of_teams = size
    max_score = (number_of_teams / 2) * (number_of_teams - 1)

    tournament = model_sts.Tournament(number_of_teams)
    tournament.initial_configuration()
    max_not_ameliored = min(int(len(tournament.list_match.neighborhood()) * (tournament.weeks/10)), 2000)

    best_eval = tournament.evaluate(tournament.list_match)/max_score
    current_configuration = tournament.list_match
    best_configuration = tournament.list_match
    best_eval_so_far = best_eval
    k=1
    kmax=max_iteration
    score=[]
    time=[]
    time_not_ameliored=0
    while k<kmax and best_eval >0:

        #input()
        #neighborhood = current_configuration.neighborhood()
        #bc = tournament.get_best_config_from_neighborhood(neighborhood)

        tournament.arbitrary_neighborhood()
        current_eval = tournament.evaluate(tournament.list_match)/max_score

        #energie = abs(best_eval-current_eval)*10
        energie = (current_eval + (current_eval-best_eval)/4)*2
        #energie =  ((current_eval/5) + (abs(current_eval-best_eval)/5)) # /(number_of_teams/6) CELLE CI ETAIT OK.
        #energie = abs(current_eval-best_eval_so_far) / 5 + (abs(current_eval - best_eval) / 5)
        temp = temperature(k,kmax)
        delta =  -energie /(temp*0.25)
        prob = proba(delta)
        rnd = random.random()

        assigning = False
        if current_eval<best_eval:
            assigning = True
        elif (prob >rnd and time_not_ameliored>max_not_ameliored) :
            assigning=True
        else:
            time_not_ameliored+=1



        if k%10000==0:
            out = "Ite " + str(k) + " Best Eval " + "{:.2f}".format(best_eval) + " Current " + "{:.2f}".format(current_eval) + " Prob " + "{:.2f}".format(prob) + " Rnd " + "{:.2f}".format(rnd) + \
                  " En " + "{:.2f}".format(energie) + " Tmp " + "{:.2f}".format(temp) + " Delta " + "{:.2f}".format(delta) + " Assigning " + str(assigning) + " Best so far "+str(best_eval_so_far)
            sys.stdout.write('\r'+out)
            sys.stdout.flush()

        if assigning :
            time_not_ameliored=0
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
    plt.ylabel("Score Configuration")
    plt.xlabel("Itération")
    #plt.scatter(time, score, s=0.01)  # ,  linestyle='solid', linewidth=1)
    plt.show()
    has_finished=False
    if best_eval_so_far==0:
        has_finished=True

    return has_finished, best_configuration


#tournament = model_sts.Tournament(number_of_teams)
#if tournament:
#    recuit_simule(tournament)

