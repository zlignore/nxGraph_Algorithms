import networkx as nx
from itertools import combinations
from Functions.bool_functions import *
from Functions.global_properties import *
import math

G = nx.erdos_renyi_graph(10, .5)
nx.draw_networkx(G)
 
def maximum_matching(G):
    for k in range(math.floor(n(G)/2), 1, -1):
        for M in combinations (E(G), k):
            if is_matching(G, list(M)) == True:
              return list(M)

print(maximum_matching(G))
