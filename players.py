import requests
from bs4 import BeautifulSoup

url = "https://www.futbin.com/24/squad-building-challenges"
html = requests.get(url)

s = BeautifulSoup(html.content, "html.parser")

results = s.find(id="content-container")
sbc_name = results.find_all("div", class_="sbc-name bold")

for name in sbc_name:
    print(name.text)
