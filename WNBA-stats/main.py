import requests
from bs4 import BeautifulSoup
import seleniumDriver as WNBA

if __name__ == "main":
    WNBAdriver = WNBA.BasketballDriver()
    WNBAdriver.print_teams()



