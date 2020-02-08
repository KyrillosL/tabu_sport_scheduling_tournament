import model_sts

def tabu(tournament ):
    tabuList = []
    tournament.initial_configuration()


    current_eval = tournament.evaluate(tournament.list_match)
    best_eval = current_eval

    print("Init eval: ", current_eval)
    best_configuration = tournament.list_match
    current_configuration = tournament.list_match

    stop_condition=False
    orig_time = 30
    time = orig_time
    max_iteration=10000000

    while not stop_condition:

        if len(tabuList)>10:
            tabuList.pop(0)

        neighborhood = current_configuration.neighborhood()

        local_best_config = tournament.get_best_config_from_neighborhood(neighborhood)

        #if len(tabuList)==len(neighborhood):
        #    print("SAME SIZE")
        #    time=0
        #else:
        while local_best_config in tabuList:
            if len(neighborhood)>1:
                neighborhood.remove(local_best_config)
                local_best_config= tournament.get_best_config_from_neighborhood(neighborhood)
            elif len(neighborhood)==1:
                local_best_config=neighborhood[0]
                neighborhood.remove(local_best_config)

        #print("already in tabu list, new local best config :",local_best_config )
        tabuList.append(local_best_config)

        current_eval = tournament.evaluate(local_best_config)
        current_configuration=local_best_config

            #print("best local config:", local_best_config, "score: ", current_eval)

        print("C ", current_eval, " B: ", best_eval, " size: ", len(tabuList), " time: ", time, " config: ",
              current_configuration)#, " best config: ", best_configuration)
        #input(":")
        if max_iteration <=0 or current_eval==0:
            stop_condition=True

        if current_eval<best_eval:
            best_eval=current_eval
            best_configuration = current_configuration

        time-=1

        if time <=0:
            print("RESETTING TABU LIST")
            current_configuration = best_configuration
            tabuList.clear()
            time=orig_time

        max_iteration-=1

    if best_eval==0:
        print("VALID SCH", current_configuration)
    else:
        print("no valid sch")





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

tournament = model_sts.Tournament(20)
if tournament:
    tabu(tournament)
