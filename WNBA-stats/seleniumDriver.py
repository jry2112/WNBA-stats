from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from dotenv import dotenv_values

config = dotenv_values(".env")
CHROMEDRIVER_PATH = config["CHROMEDRIVER_PATH"]
WNBA_TEAMS_URL = config["WNBA_TEAM_URL"]
class BasketballDriver:
    def __init__(self):
        self.service = Service(executable_path=CHROMEDRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)
        self.all_teams_url = WNBA_TEAMS_URL
        self.teams_urls = self.find_teams_urls()

    # Driver for scraping
    def get_driver(self):
        return self.driver

    # Get All Team Names and URLs from WNBA site
    def find_teams_urls(self):
        driver = self.get_driver()
        teams = {}
        driver.get(self.all_teams_url)
        driver.implicitly_wait(1)
        team_elements = driver.find_elements(By.CLASS_NAME, "stats-team-list__link")
        for team in team_elements:
            # teams = {"Team Name" : "Team URL"}
            teams[team.text] = team.get_attribute("href")
        return teams
    
    def get_teams(self):
        return self.teams_urls
    
    # Print All Team name and URLs
    def print_teams(self):
        teams = self.get_teams()
        for team in teams:
            # TeamName URL
            print(team, teams.get(team))

    # Get roster from individual team pages
    def fill_roster(self, team_url):
        driver = self.get_driver()
        teams = self.get_teams()
        roster = set()
        # Load the individual team page
        driver.get(team_url)
        player_elements = driver.find_elements(By.CLASS_NAME, "player")
        # Return the roster
        for player in player_elements:
            roster.add(player.text)
        return roster

    def fill_stats(self):
        pass



if __name__ == "__main__":
    driver = BasketballDriver()
    driver.print_teams()