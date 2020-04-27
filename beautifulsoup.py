import requests
from bs4 import BeautifulSoup

whitehouse_url = "https://www.whitehouse.gov/briefings-statements/"
whitehouse_page = requests.get(whitehouse_url)
whitehouse_src = whitehouse_page.content

wh_soup = BeautifulSoup(whitehouse_src, features="lxml")
links = wh_soup.find_all("a")
h2_links = wh_soup.find_all("h2")
print(h2_links)
# print(wh_soup.a.string)

count = 0
for link in links:
    if link.find_parent("h2"):
        count += 1
        print(str(count) + ". " + link.string)
        # print("\n")