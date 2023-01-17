import requests
from bs4 import BeautifulSoup

# WNBA Teams URL
all_teams_url = 'https://stats.wnba.com/teams/'
# fetch the raw HTML
teams_page = requests.get(all_teams_url)

soup = BeautifulSoup(teams_page.content)

# search for team links
team_links = soup.find_all("a", "stats-team-list__link")

print(team_links)