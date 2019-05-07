import networkx as nx
from Functions.weighted_functions import *

G = nx.read_weighted_edgelist('Test_Graphs/weightedG1.txt')

def prims(G, starting_vertex):
    T = nx.Graph()
    T.add_node(starting_vertex)
    while is_spanning(G, T) != True:
        e = min_cost_edge(G,T)
        T.add_edge(e[0], e[1], weight = cost(G, e))
    return T, tree_cost(G, T)
