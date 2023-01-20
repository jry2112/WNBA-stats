from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class BasketballDriver:
    def __init__(self):
        self.service = Service(executable_path="/usr/bin/chromedriver")
        self.driver = webdriver.Chrome(service=self.service)
        self.all_teams_url = 'https://stats.wnba.com/teams/'
        self.teams_urls = self.find_teams()

    # Driver for scraping
    def get_driver(self):
        return self.driver

    # Get All Team Names and URLs
    def find_teams(self):
        driver = self.get_driver()
        teams = {}
        driver.get(self.all_teams_url)
        driver.implicitly_wait(1)
        team_elements = driver.find_elements(By.CLASS_NAME, "stats-team-list__link")
        for team in team_elements:
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