from dimacs import *
import sys

sys.setrecursionlimit(100000)

def solve(v, t, c, Vis, neighbor_list):

	if(Vis[v]):return False

	Vis[v] = True

	if(Vis[t]): return True

	for (i, c_t) in neighbor_list[v]:
		if(c_t >= c):
			if(solve(i,t,c, Vis, neighbor_list)):return True

	return False


def run(file):
	(V, L) = loadWeightedGraph(file)


	L_s = [(c, x, y) for (x,y,c) in L]
	L_s.sort(reverse=True)

	neighbor_list = [[] for i in range(V+1)]

	for (x,y,c) in L:
		neighbor_list[x].append((y, c))
		neighbor_list[y].append((x, c))


	s = 1
	t = 2

	l = 0
	r = len(L) - 1

	res = -1

	while l<r:

		m = (l+r)//2	

		c = L_s[m][0]
		res = c

		Vis = [False] * (V+1)

		if(solve(s, t, c, Vis, neighbor_list)):
			r = m
		else:
			l = m+1

	return L_s[l][0]

import time 
import os
files = os.listdir("graphs/")
print(files)
c=0

for i in files:
	res = -1
	with open('graphs/' + i) as f:
		res = int(f.readline().split()[3])
	s = time.time()
	res_t = run('graphs/' + i)
	e = time.time()
	if(res == res_t):
		c+=1
		print(i + ": OK", end=' ')
	else:
		print(i + ": answer is: " + str(res) + " found: " + str(res_t), end=' ')
	print('(%f)' % (e-s))
	
print(str(c) + "/" + str(len(files)))