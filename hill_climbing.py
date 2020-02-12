import model_sts
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import random


def get_random_tabu_size(weeks):
    return random.randrange(10, weeks*50)

def hill_climbing(size =6, max_iteration=10000):
    tournament = model_sts.Tournament(size)

    tournament.initial_configuration()

    current_eval = tournament.evaluate(tournament.list_match)
    best_eval = current_eval

    print("Init eval: ", current_eval)
    best_configuration = tournament.list_match
    current_configuration = tournament.list_match

    score=[]
    tab_time=[]

    stop_condition=False
    i=0
    #print("C ", current_eval, " B: ", best_eval, " config: ", current_configuration, "INIT")

    while not stop_condition:

        neighborhood = current_configuration.neighborhood()
        local_best_config = tournament.get_best_config_from_neighborhood(neighborhood)
        current_eval = tournament.evaluate(local_best_config)


        #print("C ", current_eval, " B: ", best_eval, " config: ",current_configuration)

        if i >= max_iteration  or current_eval==0:
            stop_condition=True

        if current_eval<=best_eval:
            best_eval=current_eval
            best_configuration = current_configuration

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
    plt.show()


    return has_finished, best_configuration
