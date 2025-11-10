#Roger Blake
#this program will do the hardwood species kattis problem
import sys 

def hardwood_species():
    species_amount = {}

    species = sys.stdin.read().strip().splitlines()
    total_trees = len(species)

    for treetype in species:
        species_amount[treetype] = species_amount.get(treetype, 0) + 1
        
    for tree in sorted(species_amount):
        percentage = (species_amount[tree] / total_trees) * 100
        print(f"{tree} {percentage:.6f}")

hardwood_species()