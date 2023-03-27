import requests
from bs4 import BeautifulSoup

# Constant is in all CAPS for a data variable that will never change
URL = "https://en.wikipedia.org/wiki/List_of_holidays_by_country"

resp = requests.get(URL)

# Creating an instance of a BeautifulSoup Object, (an object has more functionality that a string ex: resp.text)
soup = BeautifulSoup(resp.text, "html.parser")

results = soup.find(id = 'ResultContainer')

all_lists = soup.find_all('li')

for country in all_lists:
    print(country, "\n")