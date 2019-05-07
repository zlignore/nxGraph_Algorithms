import networkx as nx
from Functions.global_properties import *
from Functions.local_properties import *
from Functions.bool_functions import *
from Test_Graphs import *

T = nx.read_weighted_edgelist('Test_Graphs/weightedG1.txt')
G = nx.read_weighted_edgelist('Test_Graphs/weightedG1.txt')


def cost(G, e):
    return G[e[0]][e[1]]['weight']

def is_spanning(G, H):
    return set(V(G)) == set(V(H))
def statrting_vertex(T, v):
    return v

def incident_edges(G, T, v):
    edges = []
    for i in V(T):
        if i in neighbors(T, v):
            edges.append(i)
    return edges
    
def min_cost_edge(G, T):
    
    min_edge = edges[0]
    for e in incident_edges:
        if cost(G, e) < cost(G, min_edge):
            min_edge = e
        return min_edge
    

def tree_cost(T):
    return sum(min_cost_egde(G, T) for e in T[1])
