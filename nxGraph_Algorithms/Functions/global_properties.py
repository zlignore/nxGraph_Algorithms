import networkx as nx
from Functions.local_properties import *

def n(G):
    return nx.number_of_nodes(G)

def m(G):
    return nx.number_of_edges(G)

def V(G):
    return list(nx.nodes(G))

def E(G):
    return list(nx.edges(G))

def degree_sequence(G):
    D = [vertex_degree(G, v) for v in V(G)]
    D.sort(reverse = True)
    return D

def distance_list(G, v):
    D= [[v]]
    observed = [v]
    while set(observed) != set(V(G)):
        temp_collection = []
        for w in D[-1]:
            N = neighbors(G, w)
            for x in N:
                if x not in observed:
                    observed.append(x)
                    temp_collection.append(x)
        D.append(temp_collection)
    return D

def maximum_degree(G):
    return degree_sequence(G)[0]

def minimum_degree(G):
    return degree_sequence(G)[-1]

def avg_degree(G):
    return sum(degree(G, v) for v in V(G))/n(G)

def radius(G):
    return min([eccentricity(G, v) for v in V(G)])

def diameter(G):
    return max([eccentricity(G, v) for v in V(G)])