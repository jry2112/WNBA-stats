import requests, sys
from pymongo import MongoClient
from bs4 import BeautifulSoup
import seleniumDriver as sel
import league as WNBA


def make_team(team_name, team_URL, conference):
    new_team = WNBA.Team(team_name)
    new_team.set_team_url(team_URL)
    new_team.set_conference(conference)
    return new_team

def show_players():
    WNBA_league = WNBA.League("WNBA")
    # Contains Team Names and URLs
    WNBAdriver = sel.BasketballDriver()
    teams = WNBAdriver.get_teams()
    for team in teams:
        team_url = teams.get(team)
        # Make a team object and add them to the league
        cur_team = make_team(team, team_url, '')
        WNBA_league.add_team(cur_team)

        # Find the players
        players = WNBAdriver.fill_roster(team_url)
        for player in players:
            player_name = player.split(' ', 1)
            # Make a player object and add them to the team
            cur_player = WNBA.Player(team, player_name[0], player_name[1])
            cur_team.add_player(cur_player)
    
    WNBA_league.print_teams()
    teams = WNBA_league.get_teams()
    return teams


def update_the_league():
    WNBA_league = WNBA.League("WNBA")
    # Contains Team Names and URLs
    WNBAdriver = sel.BasketballDriver()
    teams = WNBAdriver.get_teams()
    for team in teams:
        cur_team_url = teams.get(team)
        # Make a team object and add them to the league
        # find the league
        cur_league = WNBA_league.get_teams_league(team)
        cur_team = make_team(team, cur_team_url, cur_league)
        WNBA_league.add_team(cur_team)

        # Find the players
        players = WNBAdriver.fill_roster(cur_team_url)
        for player in players:
            player_name = player.split(' ', 1)
            # Make a player object and add them to the team
            cur_player = WNBA.Player(team, player_name[0], player_name[1])
            cur_team.add_player(cur_player)
    
    print("****Current WNBA Teams****")
    WNBA_league.print_teams()
    print("-------------\n")
    teams = WNBA_league.get_teams()
    for team in teams:
        print(team.get_name())
        team.print_roster()
        print("*------------------*")

    print_league_to_file(WNBA_league)
    
    return WNBA_league


def print_league_to_file(league):
    with open(f'{league.name}_league', 'w') as sys.stdout:
        print(f"****Current {league.name} Teams****")
        league.print_teams()
        print("-------------\n")
        teams = league.get_teams()
        for team in teams:
            print(team.get_name())
            team.print_roster()
            print("*------------------*")

if __name__ == "__main__":
    WNBA_League = update_the_league()

    
