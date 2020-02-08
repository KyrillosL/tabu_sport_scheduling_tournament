'''
5 Flips puis 3 Flips puis 1 flip -> Utiliser la roulette -> Mettre à jour à chaque fois la moyenne. Au départ la même probabilité. Calculer la meilleure amélioration à chaque tout.
Pour l'instant on enlève le croisement

Sous forme de tableau ecart type
voir photo
Faire des courbes lisses en faisant la moyenne des représentations

Garder les mêmes graines aléatoires.

bit flip chaque gene a 1/N chance de changer
1 flip yen a qu'un qui change sur tout le chromosome
'''

#Various import
import random
from copy import copy

import numpy as np
import sys
import tabu
import copy
np.set_printoptions(threshold=sys.maxsize)


class Agent:
    """ An agent has data (a string containing a number of "0") and the length of the string.
    For this problem, the score is the number of 1 in the string.
    We can perform various mutations on the string """

    def __init__(self, data, id):
        self.data = data


        self.id = id
        self.score =0
        self.age = 0

        self.previous_state=[]

    def add_previous_state(self, agent):
        if len(self.previous_state)>3:
            #print("ADD P")
            self.previous_state.pop(0)
        self.previous_state.append(agent)

    def __str__(self):
        #return "Agent " + str(self.id) + ", " + ''.join(self.data) + " | Score : " + str(self.get_score())
        return "Agent " + str(self.id) + ", " + str(self.data) + " | Score : " + str(self.get_score())

    def __repr__(self):
        return self.__str__()

    def __gt__(self, other):
        return (self.score < other.score)

    def __copy__(self):
        #new_data = copy.deepcopy(self.data)
        a =Agent(self.data.__copy__(), self.id)
        for ps in self.previous_state:
            a.add_previous_state(ps.__copy__())
        return a

    def get_score(self):
        self.score=self.data.evaluate(self.data.list_match)
        return self.score


class Population:
    def __init__(self, nb_agent=0, taille_agent=0):

        self.taille_agent=taille_agent
        self.nb_agent = nb_agent
        self.agents = []
        for x in range(nb_agent):
            tournament = tabu.Tournament(8)
            tournament.initial_configuration()
            self.agents.append(Agent(  tournament, x))
        self.sort()


    def sort(self):
        self.agents.sort(reverse=True)

    def __str__(self):
        string_to_return = ""
        for agent in  self.agents:
            string_to_return =string_to_return+ (agent.__str__()+"\n")
        return string_to_return

    def __repr__(self):
        return self.__str__()

    def get(self, index):
        return self.agents[index]

    def set(self, index, agent):
        self.agents[index]=agent

    def get_agents(self):
        return self.agents

    def select_best_agents(self,number_of_agent_to_return):
        new_population_to_return = Population()
        new_population_to_return.add_agents(self.agents[:number_of_agent_to_return])
        return new_population_to_return

    def select_random_agents(self,number_of_agent_to_return):
        new_population_to_return = Population()
        agents_in_population = self.agents.copy()
        for x in range(number_of_agent_to_return):
            random_number = random.randrange(0, len(agents_in_population))
            new_population_to_return.add_an_agent(agents_in_population[random_number])
            agents_in_population.remove(agents_in_population[random_number])
        return new_population_to_return

    def select_tournament_agents(self,number_of_agent_to_return, number_of_turn ):
        copy_of_agents=self.agents.copy()
        new_population_to_return = Population()
        for x in range(number_of_agent_to_return):
            population_with_best_agent = copy_of_agents[random.randrange(0, len(copy_of_agents))]
            for y in range(number_of_turn):
                population_with_new_agent=copy_of_agents[random.randrange(0, len(copy_of_agents))]
                if (population_with_best_agent.score >population_with_new_agent.score ):
                    population_with_best_agent=population_with_new_agent
            new_population_to_return.add_an_agent(population_with_best_agent, 0)
            copy_of_agents.remove(population_with_best_agent)
        return new_population_to_return

    def croisement(self, agent1, agent2):
        #@TODO : ADD ONE POINT TO SLICE
        agent1Temporaire = copy(agent1)
        agent2Temporaire = copy(agent2)

        #agent1.data = agent1.data[:int((agent1.size)/2)] #Cut the string at the half
        #agent1.data +=  (agent2.data[int((agent2.size)/2):]) #Append the end of the second one

        #agent2.data = agent2Temporaire.data[:int((agent2Temporaire.size)/2)]
        #agent2.data +=  (agent1Temporaire.data[int((agent1Temporaire.size)/2):])



    def remove_worst_agents(self, nb):
        list_to_return = []
        for x in range(nb):
            list_to_return.append(  max(self.agents).id)
            self.agents.remove(max(self.agents))
        return list_to_return

    def remove_old_agents(self, nb):

        list_to_return = []
        for x in range(nb):
            max_age = self.agents[0].age
            oldest_agent =self.agents[0]
            for a in self.agents:
                if max_age< a.age:
                    max_age=a.age
                    oldest_agent=a

            list_to_return.append(oldest_agent.id)

            self.agents.remove(oldest_agent)


        return list_to_return






    def add_agents(self,agents):
        for agent in agents:
            self.agents.insert(0,agent)

        self.sort()

    def add_an_agent(self, agent, pos):
        self.agents.append(agent)
        self.sort()



