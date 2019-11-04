from dimacs import loadDirectedWeightedGraph

class Node:
	def __init__(self):
		self.edges = {}    # słownik par mapujący wierzchołki do których są krawędzie na ich wagi

	def addEdge( self, to, weight):
		self.edges[to] = self.edges.get(to,0) + weight  # dodaj krawędź do zadanego wierzchołka
													# o zadanej wadze; a jeśli taka krawędź
													# istnieje, to dodaj do niej wagę

	def delEdge( self, to ):
		del self.edges[to]

def mergeVertices( G, x, y ):
	neibhors = list(G[y].edges.items())

	for v, w in neibhors:
		G[y].delEdge(v)
		G[v].delEdge(y)
		if(v != x):
			G[x].addEdge(v, w)
			G[v].addEdge(x, w)

	#print('deactivated vertex %d' % y)

from queue import PriorityQueue

def minimumCutPhase(G, V):
	#print(1)
	W = [0]*(V+1)
	Vis = [False] * (V+1)

	a = 1

	Q = PriorityQueue()
	Q.put((0, a))

	S = []

	while(not Q.empty()):
		w, v = Q.get()
		w = -w

		if(not Vis[v]):
			S.append(v)
			Vis[v] = True
			for (u, w) in G[v].edges.items():
				#print(u)
				if(not Vis[u]):
					W[u] += w
					Q.put((-W[u], u))

	#print(S)
	s = S[-1]
	t = S[-2]

	res = 0
	for (v,w) in G[s].edges.items():
		res += w

	mergeVertices(G, t, s)
	return res




def run(file_name):
	V, L = loadDirectedWeightedGraph(file_name)
	V_c = V
	#print(V)

	s = 1

	G = [Node() for _ in range(V+1)]
	for (x, y, w) in L:
		G[x].addEdge(y, w)
		G[y].addEdge(x, w)

	res = 1000000000000000
	while(V_c > 1):
		V_c -= 1
		res = min(res, minimumCutPhase(G, V))

	return res



import time 
import os
files = os.listdir("graphs-lab3/")
print(files)
c=0

for i in files:
	if(i == 'grid100x100'):
		continue

	res = -1
	with open('graphs-lab3/' + i) as f:
		res = int(f.readline().split()[3])
	s = time.time()
	res_t = run('graphs-lab3/' + i)
	e = time.time()
	if(res == res_t):
		c+=1
		print(i + ": OK", end=' ')
	else:
		print(i + ": answer is: " + str(res) + " found: " + str(res_t), end=' ')
	print('(%f)' % (e-s))
	
print(str(c) + "/" + str(len(files)))