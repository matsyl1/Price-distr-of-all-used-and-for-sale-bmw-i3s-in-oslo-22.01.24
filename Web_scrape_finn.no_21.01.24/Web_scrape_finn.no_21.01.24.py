# FIND PRICES FOR ALL USED FOR SALE BMW I3 LOCATED IN OSLO

# import
from bs4 import BeautifulSoup
import requests
import re

# web page containing: "merke = BMW i3, salgsform = bruktbil til salgs, område = Oslo"
url = "https://www.finn.no/car/used/search.html?location=20061&model=1.749.2000264&sales_form=1"
page = requests.get(url)
soup = BeautifulSoup(page.text, "lxml")
output = soup.prettify()

# use re.finditer() to find all matches
# matches = re.finditer("amount", output)
# for match in matches:
#     start = match.start()
#     end = match.end()
#     print(f"{start}-{end}: {output[start:end]}")


# use re.finditer() to find all matches and "r'"amount":(\d+)'" to return following digits
pattern = r'"amount":(\d+)'
matches = re.finditer(pattern, output)
for match in matches:
    start = match.start()
    end = match.end()
    prices = (f"{output[start:end]}")
    numbers = re.findall(pattern, prices)
    for number in numbers:
        x = number
        print(x)
















