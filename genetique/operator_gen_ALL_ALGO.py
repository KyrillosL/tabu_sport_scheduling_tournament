import random
import model_sts
def basic_operator(population):
    generation = 0
    while population.select_best_agents(1).get(0).score() != 1.0:
        population.croisement(population.select_best_agents(2).get(0), population.select_best_agents(2).get(1))
        #if population.select_best_agents(1).get(0).score() <= 0.75:
        population = functions.mutate(population, size - number_of_agent_to_select)
        population.sort()
        print("Generation: ", str(generation))
        print(population.select_best_agents(1).get(0))
        plt.scatter(generation, population.select_best_agents(1).get(0).score())
        generation += 1
    print("Generation: ", str(generation))

#basic_operator(population)


class Operator:
    def __init__(self, init_prob):
        self.probability = init_prob
        self.score = 0
        self.temporary_bit_to_switch = []

        self.times_used=0

        self.average_rewards = 0
        self.average_rewards_array = []
        self.weight = 1
        self.times_not_rewarded = 0

    def __str__(self):
        return  "probability: " +str(self.probability) + " | Score : " + str(self.score)

    def __repr__(self):
        return self.__str__()

    def mutate(self, agent, is_computing=False):
        print("dans le mauvais mutate")
        return "Mutate should be overrided"


    def compute_Score(self, agent):
        copy_of_agent = agent.__copy__()
        fianl_agent= self.mutate(copy_of_agent, True)
        fianl_agent.get_score()
        self.score = fianl_agent.score

    def __gt__(self, other):
        return (self.score > other.score)

    # Switch a bit in the string by an index.
    def switch_bit(self,agent, bit_to_flip):
        if (agent.data[bit_to_flip] == 0) :
            agent.data[bit_to_flip]=1
        else:
            agent.data[bit_to_flip]=0

# Flip one random bit in the string
class mutation_1_flip(Operator):

    def __init__(self, init_prob):
        Operator.__init__(self,init_prob)
        self.color=[0,0,1]
        self.pos = 0

    def __str__(self):
        return "BitFlip_1_n "+ super().__str__()

    def __repr__(self):
        return self.__str__()


    def mutate(self,agent,is_computing=False):
        #print("1N")
        #print("Using 1n, previous score: ", agent.score())

        agent_to_return = agent.__copy__()

        if is_computing:
            #bit_to_flip = random.randrange(0, agent.size)
            """
            random_periods = []
            while len(random_periods) != 2:
                random_week = random.randrange(1, agent.data.weeks)
                random_periods.clear()
                random_periods = random.sample(agent.data.list_match.get_available_period_for_week(random_week), 2)
            self.temporary_bit_to_switch.clear()
            self.temporary_bit_to_switch.append([random_periods, random_week])
            """
            random_week, random_periods = agent_to_return.data.get_random_week_and_period()
            self.temporary_bit_to_switch.clear()
            self.temporary_bit_to_switch.append([random_periods, random_week])

        agent_to_return.data.list_match.swap_periods_from_week(self.temporary_bit_to_switch[0][0], self.temporary_bit_to_switch[0][1])
        agent_to_return.get_score()
        return agent_to_return

# Flip 3 random bit in the string
class mutation_3_flip(Operator):

    def __init__(self, init_prob):
        Operator.__init__(self,init_prob)
        self.color=[1,0,0]
        self.pos = 0.50

    def __str__(self):
        return "BitFlip_3_n "+ super().__str__()

    def __repr__(self):
        return self.__str__()

    def mutate(self, agent,is_computing=False):
        #print("3N")
        agent_to_return = agent.__copy__()
        if is_computing:
            # We first select 3 random bits to flip
            # eg : >>> random.sample([1, 2, 3, 4, 5],  3)  -> [4, 1, 5]
            week_and_periods_to_switch = []
            for x in range(agent.data.teams):
                random_week, random_periods = agent_to_return.data.get_random_week_and_period()
                week_and_periods_to_switch.append( [random_week, random_periods]  )
            random_numbers = random.sample(week_and_periods_to_switch, 3)
            # flip the bits
            self.temporary_bit_to_switch.clear()
            self.temporary_bit_to_switch = random_numbers
        for x in self.temporary_bit_to_switch:
            agent_to_return.data.list_match.swap_periods_from_week(x[1], x[0])
        agent_to_return.get_score()
        return agent_to_return



class mutation_5_flip(Operator):

    def __init__(self, init_prob):
        Operator.__init__(self,init_prob)
        self.color=[0,1,0]
        self.pos = 1

    def __str__(self):
        return "BitFlip_5_n "+ super().__str__()

    def __repr__(self):
        return self.__str__()

    def mutate(self, agent,is_computing=False):
        #print("5N")
        agent_to_return = agent.__copy__()
        if is_computing:
            # We first select 3 random bits to flip
            # eg : >>> random.sample([1, 2, 3, 4, 5],  3)  -> [4, 1, 5]
            week_and_periods_to_switch = []
            for x in range(agent.data.teams):
                random_week, random_periods = agent_to_return.data.get_random_week_and_period()
                week_and_periods_to_switch.append( [random_week, random_periods]  )
            random_numbers = random.sample(week_and_periods_to_switch, 5)
            # flip the bits
            self.temporary_bit_to_switch.clear()
            self.temporary_bit_to_switch = random_numbers
        for x in self.temporary_bit_to_switch:
            agent_to_return.data.list_match.swap_periods_from_week(x[1], x[0])
        agent_to_return.get_score()
        return agent_to_return

class mutation_bit_flip(Operator):
    def mutate(self, agent):
        for x in range(self.size):
            if random.random() < (1/self.size):
                Operator.switch_bit(agent,x)