#!/usr/bin/python

from taxo_scrape import get_taxo_data

def print_tree(tree, depth=0):
    indent = "  " * depth
    for rank, name in tree:
        print("{}{}: {}".format(indent, rank, name))
        print_tree(tree[rank, name], depth+1)

class Taxo_tree():
    def __init__(self):
        self.root = {}

    def add_taxon(self, taxon_name):
        phylogeny = get_taxo_data(taxon_name)
        parent = self.root
        for rank, name in phylogeny:
            if (rank, name) not in parent:
                parent[rank, name] = {}
            parent = parent[rank, name]
            
if __name__ == "__main__":
    test = Taxo_tree()
    for name in "Human", "Bay cat", "Red Panda", "White Pine", "Dog", "Maned Wolf", "African Elephant", "Elephant shrew", "Raccoon", "Chimpanzee", "Capuchin monkey":
        test.add_taxon(name)
    print_tree(test.root)
