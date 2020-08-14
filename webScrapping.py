import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com/"
data = requests.get(url)

# print(data.headers0)
# print(data.status_code)

source_code = data.content
# print(source_code)

soup = BeautifulSoup(source_code, "html.parser")

divs = soup.find_all('div')

for div in divs:
    span = div.find_all('span')
    print(span)
