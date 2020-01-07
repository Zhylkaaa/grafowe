import networkx as nx
from dimacs import loadCNFFormula
import matplotlib.pyplot as plt

filename = 'sat/sat5_10'

(V,F) = loadCNFFormula(filename)

v = set()

for a, b in F:
	v.add(a)
	v.add(b)

G = nx.DiGraph()
G.add_nodes_from(v)

for a, b in F:
	G.add_edge(-a, b)
	G.add_edge(-b, a)


from networkx.algorithms.components import strongly_connected_components

SCC = strongly_connected_components(G)

solvable = True

H = nx.DiGraph()

t = 0

v_to_SCC = dict()
t_to_SCC = dict()

for S in SCC:
	H.add_node(t)
	t_to_SCC[t] = S
	for v in S:
		v_to_SCC[v] = t
		if (-v) in S:
			solvable = False
			break
	t+=1


solution = None

if solvable:
	solution = dict()

	n = t
	for a, b in G.edges:
		if v_to_SCC[a] != v_to_SCC[b]:
			if not H.has_edge(v_to_SCC[a], v_to_SCC[b]):
				H.add_edge(v_to_SCC[a],v_to_SCC[b])

	from networkx.algorithms.dag import topological_sort
	O = topological_sort(H)

	for t in O:
		print(t)
		for v in t_to_SCC[t]:
			if not v in solution:
				solution[v] = False
				solution[-v] = True
print(F)
print('solvable: %s' % solvable, 'solution', solution)

# test
def test(solution):
	for i in F:
		if not (solution[i[0]] or solution[i[1]]):
			print('złe rozwiązanie')
			return False

if solution is not None:
	test(solution)
