#!/usr/bin/python3

import requests
import bs4

URL_FORMAT = "https://en.wikipedia.org/w/index.php?title={}"
core_categories = ["Kingdom", "Phylum", "Class", "Order", "Family", "Genus", "Species"]

def get_taxo_data(article_name, simplified=False):
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
        taxo_data = []
        for tr in table_rows:
            td = tr.find_all('td')
            if len(td) == 2:
                text = [item.text.strip().replace("\xa0", " ") for item in td]
                if text[0][-1] == ":":
                    text[0] = text[0][:-1]
                    if not simplified or text[0] in core_categories:
                        taxo_data.append(text)
        return taxo_data
    except:
        return []

def run_tests():
    import doctest
    doctest.testmod(verbose=True)

if __name__ == "__main__":
    from sys import argv, stderr
    
    if len(argv) != 2:
        print("Usage: {} article_name".format(argv[0], file=stderr))
        exit(-1)
    print(get_taxo_data(argv[1]))

