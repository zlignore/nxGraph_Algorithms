import networkx as nx
from Functions.weighted_functions import *

T = nx.read_weighted_edgelist('Test_Graphs/weightedG1.txt')
G = nx.read_weighted_edgelist('Test_Graphs/weightedG1.txt')

def prims(G, starting_vertex):
    T = nx.Graph()
    T.add_node(starting_vertex)
    while is_spanning(G, T) == False:
        T.add_node(min_cost_edge(G, T))
    return T, tree_cost(T)
