#!/usr/bin/python3

import requests
import bs4

URL_FORMAT = "https://en.wikipedia.org/w/index.php?title={}"

def get_taxo_data(article_name):
    try:
        page = requests.get(URL_FORMAT.format(argv[1])).content.decode("utf-8")
        soup = bs4.BeautifulSoup(page, "html5lib")
        table = soup.find("table", {"class": "infobox biota"})
        table_rows = table.find_all('tr')
        taxo_data = {}
        for tr in table_rows:
            td = tr.find_all('td')
            if len(td) == 2 and td[0].text.strip()[-1] == ":":
                row = [i.text.strip().replace("\xa0", " ").replace(":", "") for i in td]
                taxo_data[row[0]] = row[1]
        return taxo_data
    except:
        return {}

if __name__ == "__main__":
    from sys import argv, stderr
    if len(argv) < 2:
        argv.append("human")
    print(get_taxo_data(argv[0]))
#print(tag)

