import networkx as nx
from itertools import combinations
from Functions.bool_functions import *
from Functions.global_properties import *
import math

 
def maximum_matching(G):
    for k in range(math.floor(n(G)/2), 1, -1):
        for M in combinations (E(G), k):
            if is_matching(G, list(M)) == True:
              return list(M)
