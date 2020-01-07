import networkx as nx
from dimacs import loadDirectedWeightedGraph
import matplotlib.pyplot as plt

G = nx.DiGraph()

filename = 'graphs-lab2/flow/clique5'
(V, L) = loadDirectedWeightedGraph(filename)

v = [i for i in range(1, V+1)]

G.add_nodes_from(v)

for a, b, c in L:
	G.add_edge(a, b)
	G[a][b]['capacity'] = c

from networkx.algorithms.flow import maximum_flow

print(maximum_flow(G, 1, V)[0])
