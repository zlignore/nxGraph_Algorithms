import networkx as nx
from Functions.global_properties import *
from Functions.local_properties import *
from Functions.bool_functions import *
from Test_Graphs import *

def cost(G, e):
    """Returns the cost of a given edge"""
    return G[e[0]][e[1]]['weight']

def is_spanning(G, H):
    """Confirms if the tree T is spanning to the graph G"""
    return set(V(G)) == set(V(H))

def incident_edges(G, T):
    """Returns a list of edges adjacent to the starting vertex"""
    edges = []
    for e in E(G):
        if e[0] in V(T) or e[1] in V(T):
            if e[0] not in V(T) or e[1] not in V(T):
                edges.append(e)
    return edges
    
def min_cost_edge(G, T):
    """Returns the edge with the lowest cost"""
    edges = incident_edges(G, T)
    min_edge = edges[0]
    for e in edges:
        if cost(G, e) < cost(G, min_edge):
            min_edge = e
    return min_edge
    
def tree_cost(G, T):
    """Returns the cost of all the edges in the tree T"""
    return sum([cost(G, e) for e in E(T)])
