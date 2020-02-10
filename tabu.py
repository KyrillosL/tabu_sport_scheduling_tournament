import model_sts
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import random


def get_random_tabu_size(weeks):
    return random.randrange(10, weeks*50)

def tabu(size =6, max_iteration=10000):
    tournament = model_sts.Tournament(size)
    tabuList = []
    tournament.initial_configuration()


    current_eval = tournament.evaluate(tournament.list_match)
    best_eval = current_eval

    print("Init eval: ", current_eval)
    best_configuration = tournament.list_match
    current_configuration = tournament.list_match

    score=[]
    tab_time=[]

    stop_condition=False
    tabu_size=get_random_tabu_size(tournament.weeks)
    orig_time = min(int(len(current_configuration.neighborhood()) * (tournament.weeks/10)), 2000)
    #orig_time=30
    time = orig_time
    i=0


    while not stop_condition:

        if len(tabuList)>tabu_size:
            tabuList.pop(0)

        neighborhood = current_configuration.neighborhood()

        local_best_config = tournament.get_best_config_from_neighborhood(neighborhood)


        while local_best_config in tabuList:
            if len(neighborhood)>1:
                neighborhood.remove(local_best_config)
                local_best_config= tournament.get_best_config_from_neighborhood(neighborhood)
            elif len(neighborhood)==1:
                local_best_config=neighborhood[0]
                neighborhood.remove(local_best_config)

        tabuList.append(local_best_config)

        current_eval = tournament.evaluate(local_best_config)
        current_configuration=local_best_config

        print("C ", current_eval, " B: ", best_eval, " size: ", len(tabuList), " time: ", time, " config: ",current_configuration)

        if i >= max_iteration  or current_eval==0:
            stop_condition=True

        if current_eval<best_eval:
            best_eval=current_eval
            best_configuration = current_configuration

        else:
            time-=1

        if time <=0:
            print("RESETTING TABU LIST")
            current_configuration = best_configuration
            tabuList.clear()
            tabu_size = get_random_tabu_size(tournament.weeks)
            time=orig_time

        #max_iteration-=1
        i+=1
        score.append(best_eval)
        tab_time.append(i)

    has_finished=False
    if best_eval==0:
        print("VALID SCH", current_configuration)
        has_finished=True
    else:
        print("no valid sch")

    plt.plot(tab_time,score,linestyle='solid', linewidth=0.5)
    plt.ylabel("Score Configuration")
    plt.xlabel("Itération")
    #plt.scatter(time, score, s=0.01)  # ,  linestyle='solid', linewidth=1)
    #plt.show()


    return has_finished, best_configuration




'''
if tournament:

    tabu(tournament)

    tournament.initial_configuration()
    print(tournament)
    eval = tournament.evaluate_neighborhood()
    while eval != 0:
        eval = tournament.evaluate_neighborhood()
    print(tournament)

    tournament.arbitrary_neighborhood()
    print("AFTER SWAAAPP")
    print(tournament)
    print(tournament.evaluate(tournament.list_match))


    while tournament.evaluate(tournament.list_match)!=0:
        tournament.arbitrary_neighborhood()
        print (tournament.evaluate(tournament.list_match))
    print(tournament)
'''

#tournament = model_sts.Tournament(12)
#if tournament:
#    tabu(tournament)
