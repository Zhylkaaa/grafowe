from dimacs import loadDirectedWeightedGraph
from collections import deque

def bfs(GR, s, t, c, f, A, V):
	Vis = [False] * (V+1)
	Vis[s] = True
	parent = [-1] * (V+1)
	Q = deque()
	Q.append(s)

	while(Q):
		v = Q.popleft()

		if(v == t):
			p = []
			c_res = 1000000000
			prev_v = -1

			while(v != -1):
				p.append(v)
				prev_v = v
				v = parent[v]
				if(v != -1):
					if((v,prev_v) in A):
						c_res = min(c_res, c[(v, prev_v)] - f[(v, prev_v)])
					else:
						c_res = min(c_res, f[(prev_v, v)])
			p.reverse()
			return (c_res, p)

		for u in GR[v]:
			if(not Vis[u]):
				if((v,u) in A):
					if(c[(v,u)] - f[(v,u)] > 0):
						Q.append(u)
						Vis[u] = True
						parent[u] = v
				else:
					if(f[(u,v)] > 0):
						Q.append(u)
						Vis[u] = True
						parent[u] = v
	return (None, None)


def run(file_name):
	V, L = loadDirectedWeightedGraph(file_name)
	G = [set() for i in range(V+1)]
	c = dict()
	f = dict()
	A = dict()

	for (x,y,w) in L:
		G[x].add(y)
		A[(x,y)] = 1
		c[(x,y)] = w
		f[(x,y)] = 0

	s = 1
	t = V

	GR = G.copy()

	(c_m, p) = bfs(GR, s, t, c, f, A, V)
	while p != None:
		v = p[0]

		for u in p[1:]:
			if((v,u) in A):
				f[(v,u)] += c_m
				GR[u].add(v)
			else:
				f[(u,v)] -= c_m
			v = u
		(c_m, p) = bfs(GR, s, t, c, f, A, V)

	res = 0

	for u in G[1]:
		res += f[(1, u)]
	return res



import time 
import os
files = os.listdir("graphs-lab2/flow/")
print(files)
c=0

for i in files:
	res = -1
	with open('graphs-lab2/flow/' + i) as f:
		res = int(f.readline().split()[3])
	s = time.time()
	res_t = run('graphs-lab2/flow/' + i)
	e = time.time()
	if(res == res_t):
		c+=1
		print(i + ": OK", end=' ')
	else:
		print(i + ": answer is: " + str(res) + " found: " + str(res_t), end=' ')
	print('(%f)' % (e-s))
	
print(str(c) + "/" + str(len(files)))
