#!/usr/bin/python3

import requests
import bs4

URL_FORMAT = "https://en.wikipedia.org/w/index.php?title={}"

def get_taxo_data(article_name):
    """ (str) -> dict of {str:str}
    Given the name of a Wikipedia article on a species or other taxon (i.e. an
    article containing a table whose class attribute is exactly "infobox biota"),
    return a dictionary mapping taxonomic category type to the relevant taxon.

    In the event that `article_name` does not refer to a Wikipedia article
    containing such a table, or the data is otherwise not retrievable, return
    an empty dict.

    >>> get_taxo_data("bogus_name") == {}
    True
    >>> expected = {'Kingdom': 'Animalia', 'Phylum': 'Chordata', 'Class':\
    'Mammalia', 'Order': 'Primates', 'Suborder': 'Haplorhini', 'Infraorder':\
    'Simiiformes', 'Family': 'Hominidae', 'Subfamily': 'Homininae', 'Tribe':\
    'Hominini', 'Genus': 'Homo', 'Species': 'H. sapiens'}
    >>> expected == get_taxo_data("Human")
    True
    """
    try:
        page = requests.get(URL_FORMAT.format(article_name)).content.decode("utf-8")
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

def run_tests():
    import doctest
    doctest.testmod(verbose=True)

if __name__ == "__main__":
    from sys import argv, stderr
    if len(argv) < 2:
        argv.append("human")
    print(get_taxo_data(argv[0]))
#print(tag)

