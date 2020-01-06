import random
import numpy as np
import copy

class Match:
    def __init__(self, team1, team2, week, period):
        self.team1 = team1
        self.team2 = team2
        self.week = week
        self.period = period

    def __str__(self):
        return str(self.team1) + " vs " + str(self.team2) + " w: "+ str(self.week)+" p: "+ str(self.period)

    def __repr__(self):
        return __str__()

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Match):
            return (self.team1 == other.team1 and self.team2 == other.team2) or (self.team2 == other.team1 and self.team1 == other.team2)
        return False







class List_Match:
    def __init__(self, weeks, periods):
        self.matchs = []
        self.periods= periods
        self.weeks = weeks

    def __eq__(self, other):
        """Overrides the default implementation"""
        #print("IN EQ")
        if isinstance(other, List_Match):
            #print("EQ")
            return self.matchs == other.matchs and self.periods == other.periods and self.weeks==other.weeks
        #print("NOT EQUAL")
        return False

    def __str__(self):
        '''
        #string_to_return= str(self.periods)+ str(self.weeks)+"\n"
        string_to_return = ""
        for i in range(1,self.weeks+1):
            to_print = (x for x in self.matchs if x.week ==i)
            string_to_return += "Week : "
            string_to_return+=str(i)
            string_to_return+="\n"
            for j in to_print:
                string_to_return+= str(j)
                string_to_return+="\n"
            string_to_return += "\n"
        return string_to_return
        '''
        string_to_return = ""
        for m in self.matchs:
            string_to_return+=str(m.team1)
            string_to_return+=str(m.team2)
            string_to_return += " "
        return  string_to_return

    def __repr__(self):
        '''
        # string_to_return= str(self.periods)+ str(self.weeks)+"\n"
        string_to_return = ""
        for i in range(1, self.weeks + 1):
            to_print = (x for x in self.matchs if x.week == i)
            string_to_return += "Week : "
            string_to_return += str(i)
            string_to_return += "\n"
            for j in to_print:
                string_to_return += str(j)
                string_to_return += "\n"
            string_to_return += "\n"
        return string_to_return
        '''
        string_to_return = ""
        for m in self.matchs:
            string_to_return+=str(m.team1)
            string_to_return+=str(m.team2)
            string_to_return += " "
        return  string_to_return



    def append(self, match):
        self.matchs.append(match)

    def add_diagonal_from_graph(self,i,j,k,l, list_period ):
        orig_size = len(self.matchs)

        if self.get_week_from_match(i, j) != None:

            for p in list_period:
                if p not  in self.get_available_period_for_week(self.get_week_from_match(i, j)):
                    #print("AVAILABLE:", p)
                    match = Match(k, l, self.get_week_from_match(i, j), p)
                    #list_period.remove(p)
                    if not self.in_list(match):
                        self.matchs.append(match)
                    break

        if self.get_week_from_match(k, l) != None:
            for p in list_period:
                if p not  in self.get_available_period_for_week(self.get_week_from_match(k, l)):
                    #print("AVAILABLE2:", p)
                    match = Match(i, j, self.get_week_from_match(k, l), p)
                    #list_period.remove(p)
                    if not self.in_list(match):
                        self.matchs.append(match)
                    break

        #list_period.pop(0)
        return orig_size != len(self.matchs)

    def get_week_from_match(self, team1, team2):
        for x in self.matchs:
            if ( x.team1 == team1 and x.team2 == team2)  or ( x.team2 == team1 and x.team1 == team2) :
                return x.week

    def get_week_from_team(self, team):
        list = []
        for x in self.matchs:
            if  x.team1 == team or x.team2 == team:
                list.append(x.week)
        return list



    def remaining_week_to_assign(self,i, teams ):
        for x in range(1,teams) :
            if x not in self.get_week_from_team(i):
                return x

    def get_available_period_for_week(self, week):
        list = []
        for x in self.matchs:
                if x.week==week:
                    if x.period not in list:
                        list.append(x.period)
        return list

    def get_match(self,period, week ):
        for x in self.matchs:
            if x.period == period and x.week == week:
                return x

    def get_occurence_team_in_period(self, t,p):
        number=0
        for m in self.matchs:
            if (m.team1 ==t or m.team2 == t ) and m.period==p:
                number+=1
        return number

    def swap_periods_from_week(self, periods, week):
        period_1= periods[0]
        period_2= periods[1]
        #print("swapping period ", period_1," and period ", period_2,"from week ", week)
        tmp_match = copy.deepcopy( self.get_match(period_1, week))
        #print(tmp_match)

        m1 = self.get_match(period_1, week)
        m2 = self.get_match(period_2, week)

        m1.team1 = m2.team1
        m1.team2 = m2.team2

        m2.team1 = tmp_match.team1
        m2.team2 = tmp_match.team2


    def get_size(self):
        return len(self.matchs)
    def get_match_from_index(self, i):
        return self.matchs[i]

    def in_list(self, match):
        return match in self.matchs

    def neighborhood(self):

        matrix_to_return = []
        for week in range(1, self.weeks + 1):
            for j in range(1, self.periods + 1):
                for k in range(1, self.periods + 1):
                    if k>j:
                        copy_of_configuration = copy.deepcopy(self)
                        copy_of_configuration.swap_periods_from_week([j, k], week)
                        matrix_to_return.append(copy_of_configuration)
        #print(matrix_to_return)
        return matrix_to_return


class Tournament:
    def __new__(cls, number_of_teams):
        if number_of_teams % 2 != 0:
            return None
        # create a new instance and set attributes on it
        instance = super().__new__(cls)  # empty instance
        return instance

    def __init__(self, number_of_teams):

        print("Creating Tournament")
        self.teams = number_of_teams
        self.weeks = number_of_teams-1
        self.periods = int(number_of_teams/2)
        self.list_match = List_Match(self.weeks, self.periods)


    def initial_configuration(self):
        list_of_period= []
        '''
        for p in range(1,self.periods+1):
            for w in range(1,self.weeks+1):
                list_of_period.append( p )
        '''

        for p in range(1,self.periods+1):
            list_of_period.append(p)
        #print(list_of_period)

        #5 matchs de 1, 5 de 2, 5 de 3

        #SIDES
        for i in range(0,self.teams-1):
            if i==self.teams-2:
                match = Match( i+1, 1,1,1)
                #list_of_period.pop(0)
            else:
                match = Match(i+1,i+2,i+2, 1)
                #list_of_period.pop(0)
            self.list_match.append(match)

        #print(list_of_period)

        # DIAGONALS
        for i in range(1,self.teams):
            for j in range(1,self.teams) :
                #team 1 doesn't go against team 1
                if i!=j:
                    for k in range(1, self.teams ):
                        for l in range(1, self.teams):
                            if k != l:
                                if i+j ==k+l or ((i==1) and  (self.teams +j ==k+l) ):
                                    self.list_match.add_diagonal_from_graph(i,j,k,l, list_of_period)



        #print(list_of_period)
        #We add the last team

        for i in range(1,self.teams):
            match = Match( i, self.teams ,  self.list_match.remaining_week_to_assign(i, self.teams) , self.periods)
            #list_of_period.pop(0)
            self.list_match.append(match)


    def arbitrary_neighborhood(self):
        random_periods=[]
        while len(random_periods)!=2:
            random_week = random.randrange(1, self.weeks)
            random_periods.clear()
            random_periods= random.sample(self.list_match.get_available_period_for_week(random_week),2)
        #print("SWAPPING : ", random_periods, random_week)
        self.list_match.swap_periods_from_week(random_periods ,random_week)




    def evaluate(self, list_match):
        #print(list_match)
        result = 0
        for p in range(1,self.periods+1):
            for t in range(1, self.teams+1):
                occurence = list_match.get_occurence_team_in_period(t,p)
                #print("p : ", p, " t : ", t, " occ : ", occurence)
                if occurence > 2:
                    result += occurence-2
        #print (result)
        return result







        best_configuration =self.evaluate(self.list_match)
        #print("INIT SCORE: ", best_configuration)
        #print("COPY: ", copy_of_configuration)
        #x = self.weeks*self.teams
        #for i in range(x):
        #    for j in range(x):

        #matrix = [[10000 for x in range(1,self.periods+1)] for y in range(1,self.weeks+1)]
        '''
        for week in range(1,self.weeks+1):
            for j in range(1,self.periods+1):
                for k in range(1,self.periods+1):
                    if k>j:
                        #print("NEW")
                        copy_of_configuration = copy.deepcopy(self.list_match)
                        #print(k,j)
                        #print("AVANT ", copy_of_configuration)
                        copy_of_configuration.swap_periods_from_week([j, k], week)
                        #print("APRES ", copy_of_configuration)
                        #matrix[week-1][j-1]= self.evaluate(copy_of_configuration)
                        current_conf = self.evaluate(copy_of_configuration)
                        #print("current_conf", current_conf, "week ", week)
                        if  current_conf< best_configuration:
                            best_configuration=current_conf

        for week in range(1,self.weeks+1):
            for j in range(1,self.periods+1):
                for k in range(1,self.periods+1):
                    if k>j:
                        copy_of_configuration = copy.deepcopy(self.list_match)
                        copy_of_configuration.swap_periods_from_week([j, k], week)
                        if best_configuration==self.evaluate(copy_of_configuration):
                            #print("BEST CONFIG w: ", week, " score: " ,best_configuration )
                            if should_update_list_match:
                                self.list_match= copy_of_configuration
                            break


        '''
        '''
        for j in range(0,self.weeks):
            for k in range(0,self.periods):
                if best_configuration> matrix[j][k]:
                    best_configuration=matrix[j][k]
                    copy_of_configuration = copy.deepcopy(self.list_match)
                    copy_of_configuration.swap_periods_from_week([j+1, k+1], week)
                    print("new best")
        '''
        '''
        if should_update_list_match:
            print("UPDATE")
            for week in range(1,self.weeks+1):
                for j in range(1,self.periods+1):
                    for k in range(1,self.periods+1):
                        if k>j:
                            if matrix[week-1][j-1]==best_configuration:
                                #print(self.list_match)
                                self.list_match.swap_periods_from_week([j,k], week)
                                #print("fin")
                                break
        '''

        #print("BESST",best_configuration)
        #print("Copy swapped:",copy_of_configuration)
        #return best_configuration, self.list_match

    def __str__(self):
        #string_to_return ="\t\tPeriods\n"
        #for i in range(self.weeks):
            #for j in range(self.periods):

                #print("dans le str")
                #string_to_return+= "\t"+str(self.list_match[i][j])
            #string_to_return+='\n'
        #return string_to_return +'\n\t'.join([' | '.join([str(item) for item in row]) for row in self.list_match])
        #return '\n'.join([' | '.join([str(item) for item in row]) for row in self.list_match])
        string_to_return =""
        """
        for i in range(self.list_match.get_size()):
            string_to_return+=str(self.list_match.get_match_from_index(i))
            string_to_return+="\n"
        return string_to_return
        """
        return str(self.list_match)



    def __repr__(self):
        return __str__()


def get_best_config_from_neighborhood(neighborhood):

    local_best_config = neighborhood[0]
    local_best_value = tournament.evaluate(local_best_config)
    for c in neighborhood:
        if tournament.evaluate(c) < tournament.evaluate(local_best_config):
            local_best_config = c
            local_best_value = tournament.evaluate(c)

    list_config_with_best_value= []
    for c in neighborhood:
        if local_best_value== tournament.evaluate(c):
            list_config_with_best_value.append(c)

    local_best_config= random.choice(list_config_with_best_value)

    return local_best_config


'''
generate_new_eval=True
while generate_new_eval:
    for m in tabuList:
        if current_eval[1]==m:
            #print("EQ")
            current_eval = tournament.evaluate_neighborhood(False)
            #print(m)
            #print (new_eval[1])
            continue
    generate_new_eval=False
'''
'''
while current_eval in tabuList:
    print("in tabu list")
    current_eval = tournament.evaluate_neighborhood(False)

tabuList.append(current_eval[1])
'''

def tabu(tournament ):
    tabuList = []
    tournament.initial_configuration()


    current_eval = tournament.evaluate(tournament.list_match)
    best_eval = current_eval

    print("Init eval: ", current_eval)
    best_configuration = tournament.list_match
    current_configuration = tournament.list_match

    stop_condition=False

    time = 30
    max_iteration=100

    while not stop_condition:

        if len(tabuList)>10:
            tabuList.pop(0)

        neighborhood = current_configuration.neighborhood()

        local_best_config = get_best_config_from_neighborhood(neighborhood)

        #if len(tabuList)==len(neighborhood):
        #    print("SAME SIZE")
        #    time=0
        #else:
        while local_best_config in tabuList:
            if len(neighborhood)>1:
                neighborhood.remove(local_best_config)
                local_best_config= get_best_config_from_neighborhood(neighborhood)
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
            time=30



        max_iteration-=1

    if best_eval==0:
        print("VALID SCH", current_configuration)
    else:
        print("no valid sch")

#tabu()


tournament = Tournament(10)
if tournament:

    tabu(tournament)
    '''
    tournament.initial_configuration()
    print(tournament)
    eval = tournament.evaluate_neighborhood()
    while eval != 0:
        eval = tournament.evaluate_neighborhood()
    print(tournament)
    '''
    '''
    tournament.arbitrary_neighborhood()
    print("AFTER SWAAAPP")
    print(tournament)
    print(tournament.evaluate(tournament.list_match))


    while tournament.evaluate(tournament.list_match)!=0:
        tournament.arbitrary_neighborhood()
        print (tournament.evaluate(tournament.list_match))
    print(tournament)
    '''

