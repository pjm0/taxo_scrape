#!/usr/bin/python3

from taxo_scrape import get_taxo_data

class Taxo_tree():
    def __init__(self, simplified=False):
        self.root = {}
        self.simplified = simplified

    def __str__(self):
        return self.subtree_to_str(self.root)

    def subtree_to_str(self, subtree, depth=0):
        indent = "  " * depth
        result = ""
        for rank, name in subtree:
            result += "{}{}: {}\n".format(indent, rank, name)
            result += self.subtree_to_str(subtree[rank, name], depth+1)
        return result

    def add_taxon(self, taxon_name):
        phylogeny = get_taxo_data(taxon_name, self.simplified)
        parent = self.root
        for rank, name in phylogeny:
            if (rank, name) not in parent:
                parent[rank, name] = {}
            parent = parent[rank, name]
            
if __name__ == "__main__":
    from sys import argv
    from getopt import gnu_getopt as getopt
    args = argv[1:]
    optlist, args = getopt(args, "", ["simple"])
    opts =  dict(optlist)
    simplified = "--simple" in opts
    tree = Taxo_tree(simplified)
    for name in args:
        tree.add_taxon(name)
    print(tree)
