from Functions.bool_functions import is_dominating
from Functions.global_properties import V, n
from itertools import combinations
import networkx as nx


def minimum_dominating(G):
    for k in range(1, n(G)):
        for S in combinations(V(G), k):
            if is_dominating(G, list(S)) == True:
                return list(S)
            
def domination_number(G):
    return len(minimum_dominating(G))
