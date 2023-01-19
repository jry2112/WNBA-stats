from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class BasketballDriver:
    def __init__(self):
        self.service = Service(executable_path="/usr/bin/chromedriver")
        self.driver = webdriver.Chrome(service=self.service)
        self.all_teams_url = 'https://stats.wnba.com/teams/'
        self.teams_urls = self.find_teams()

    def get_driver(self):
        return self.driver

    def find_teams(self):
        driver = self.get_driver()
        teams_dict = {}
        driver.get(self.all_teams_url)
        driver.implicitly_wait(10)
        team_elements = driver.find_elements(By.CLASS_NAME, "stats-team-list__link")
        for team in team_elements:
            teams_dict[team.text] = team.get_attribute("href")
        return teams_dict
    
    def get_teams(self):
        return self.teams_urls
    
    def print_teams(self):
        teams = self.get_teams()
        for team in teams:
            # TeamName URL
            print(team, teams.get(team))


if __name__ == "__main__":
    driver = BasketballDriver()
    driver.print_teams()