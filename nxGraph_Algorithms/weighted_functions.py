import networkx as nx
from Functions.global_properties import *
from Functions.local_properties import *
from Functions.bool_functions import *
from Test_Graphs import *

def cost(G, e):
    return G[e[0]][e[1]]['weight']

def is_spanning(G, H):
    return set(V(G)) == set(V(H))

def incident_edges(G, T):
    edges = []
    for e in E(G):
        if e[0] in V(T) or e[1] in V(T):
            if e[0] not in V(T) or e[1] not in V(T):
                edges.append(e)
    return edges
    
def min_cost_edge(G, T):
    edges = incident_edges(G, T)
    min_edge = edges[0]
    for e in edges:
        if cost(G, e) < cost(G, min_edge):
            min_edge = e
    return min_edge
    
def tree_cost(G, T):
    return sum([cost(G, e) for e in E(T)])
