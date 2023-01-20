class League:
    # Leaugue consists of 11 teams split between Eastern and Western Conference
    def __init__(self):
        self.teams = []
        self.eastern_conf = []
        self.western_conf = []

    # Add a Team to the League
    def add_team(self, team):
        self.teams.append(team)
    
    # Get list of Teams
    def get_teams(self):
        return self.teams

    # Get Eastern Conference Teams
    def get_eastern_conf(self):
        return self.eastern_conf

    # Get Eastern Conference Teams
    def get_western_conf(self):
        return self.eastern_conf

    # Print all Team Names    
    def print_teams(self):
        for team in self.teams:
            print(team.name)
            



class Player:
    def __init__(self, team, first_name, last_name):
        self.url = None
        self.team = team
        self.first_name = first_name
        self.last_name = last_name
        self.number = None
        self.position = None
        self.height = None
        self.age = None
        self.stats = {}


    # Get the player's dynamic URL
    def get_url(self):
        return self.url

    # Set the player's dynamic URL
    def set_url(self, player_url):
        self.url = player_url

    # Get the player's name FIRST LAST
    def get_name(self):
        name = self.first_name + ' ' + self.last_name
        return name

    # Update a player's stats
    def 

class Team:
    def __init__(self, name):
        self.name = name
        self.team_url = None
        self.conference = None
        self.roster = []

    def get_name(self):
        return self.name
    
    def get_team_url(self):
        return self.team_url

    def set_team_url(self, url : str):
        self.team_url = url

    def get_conference(self):
        return self.conference

    def set_conference(self, conference : str):
        self.conference = conference

    def get_roster(self):
        return self.roster

    def print_roster(self):
        for player in self.roster:
            print(player.first_name, player.last_name)
    
    def add_player(self, player : Player):
        self.roster.append(player)

    def get_player(self, first_name : str, last_name : str):
        for player in self.roster:
            if player.first_name == first_name and player.last_name == last_name:
                return player
        return None
