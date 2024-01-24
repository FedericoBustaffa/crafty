import requests
import bs4
import time


base_url = "https://bitinfocharts.com/bitcoin/address/"
headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    + " (KHTML, like Gecko) Chrome/61.0.3163.100Safari/537.36"
}

r = requests.get(base_url + "15GWLfGNuqbSvP7EqYAvwhEs99vjgUXksC")
soup = bs4.BeautifulSoup(r.text, "html.parser")
table = soup.find("table", {"class": "table table-striped table-condensed"})
if isinstance(table, bs4.Tag):
    print(table.text)
    small = table.find("small")
    if isinstance(small, bs4.Tag):
        print(small.get_text())
