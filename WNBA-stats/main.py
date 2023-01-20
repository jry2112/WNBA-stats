import requests
from bs4 import BeautifulSoup
import seleniumDriver as sel
import league as WNBA

def make_team(team_name, team_URL, conference):
    new_team = WNBA.Team(team_name)
    new_team.set_team_url(team_URL)
    new_team.set_conference(conference)
    return new_team


if __name__ == "__main__":
    WNBA_league = WNBA.League()
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
    for team in teams:
        print(team.get_name())
        team.print_roster()

