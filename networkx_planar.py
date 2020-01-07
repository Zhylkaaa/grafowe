import networkx as nx
from dimacs import loadWeightedGraph
import matplotlib.pyplot as plt

G = nx.Graph()

filename = 'graphs-lab6/plnar/clique20'

(V, L) = loadWeightedGraph(filename)

v = [i for i in range(V+1)]

G.add_nodes_from(v)

for a, b, w in L:
	G.add_edge(a,b)

from networkx.algorithms.planarity import check_planarity

print(check_planarity(G)[0])

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
plt.show()
