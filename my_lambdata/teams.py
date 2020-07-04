# teams.py

class Team():
    def __init__(self, name, city, roster=['Player1']):
        # these are attributes / nouns
        self.name = name
        self.city = city
        self.roster = roster

    # this is a property / noun
    # the @property decorator allows us to invoke this without trailing parentheses
    @property
    def full_name(self):
        return f"{team.city} {team.name}"

    # this is a method / verb
    def advertise(self):
        print("PLEASE COME TO", self.city.upper(), "TO SEE US PLAY")

    # this method doesn't require any information about the specific instance itself
    # the @staticmethod decorator allows us to omit passing "self" as a param
    @staticmethod
    def advertise_generically():
        print("PLEASE COME TO OUR GAMES")

class BaseballTeam():
    def __init__(self, name, city, starting_pitcher, roster=['Player1']):
        # these are attributes / nouns
        self.name = name
        self.city = city
        self.roster = roster
        self.starting_pitcher = starting_pitcher
    
    @property 
    def advertise(self):
        print("PLEASE COME TO", self.city.upper(), "TO SEE US PLAY")

    @staticmethod
    def advertise_generically():
        print("PLEASE COME TO OUR GAMES")

   
    
if __name__ == "__main__":

    teams = [
        {"city": "New York", "name": "Yankees", 'starting_pitcher': 'Jose'},
        {"city": "New York", "name": "Mets", 'starting_pitcher': 'Raymond'},
        {"city": "Washington", "name": "Nationals", 'starting_pitcher': 'Ian'},
        {"city": "Kansas City", "name": "Royals", 'starting_pitcher': 'Alex'},
        {"city": "Boston", "name": "Red Sox", 'starting_pitcher': 'John'}    
    ]

    for d in teams:
        #print(team["city"] + " " + team["name"])
        #print(full_name(team)) #> functional approach
        team = Team(d["name"], d["city"], d['starting_pitcher'])
        print(team.name)
        print(team.full_name) #> OOP (invoke the method on the object)
        team.advertise()
        print(team.roster)
        #print(team.starting_pitcher)