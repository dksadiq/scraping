import requests
from bs4 import BeautifulSoup

whitehouse_url = "https://www.whitehouse.gov/briefings-statements/"
whitehouse_page = requests.get(whitehouse_url)
whitehouse_src = whitehouse_page.content

wh_soup = BeautifulSoup(whitehouse_src, "lxml")
links = wh_soup.find_all("a")
print(links)