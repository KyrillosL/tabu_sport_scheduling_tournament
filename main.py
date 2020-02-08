import algorithme_genetique as ag

import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt




#DIRE : Le 3N / 5N marche mieux que loracle car ne tombe pas dans les miniums locaux.


parametres_algo = {
"nombre_agents_par_population":1000,
"taille_agent":8,
"nb_indiv_to_select":20
}


ag = ag.Algorithme_genetique(parametres_algo)

#0 = Oracle Myope OK MARCHE BIEN
#1 = roulette fixe OK RESULTAT ATTENDU
#2 = roulette adaptive NON
#3= adaptive poursuit OK MARCHE BIEN
#4=ucb JOUER SUR LA FENETRE DE REWARD !!!!! DANS LE RAPPORT
#5=Exp3 NE MARHCE QU'AVEC LES NON DEGRADNATS
#6= BASIC 3N VRAIMENT BIEN
#refresh_rate_counter=parametres_algo["taille_agent"]/10

ag.solve(method=6, realtime_plot=False, refresh_rate_plot=1, realtime_counter=True,refresh_rate_counter=1, keep_degrading=True, one_indiv=False, stop_after=10000,
                           number_of_pass=1, all_score = False)
