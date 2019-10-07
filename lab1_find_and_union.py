from dimacs import *
import sys

sys.setrecursionlimit(100000)

p = dict()

def union(x, y):
	global p
	a = find(x)
	b = find(y)

	if(a!=b):
		p[a] = b

def find(x):
	global p
	if(p[x] != x):
		v = p[x]
		p[x]=find(v)
		return p[x]
	else:
		return x

def run(file):
	global p
	(V, L) = loadWeightedGraph(file)


	L_s = [(c, x, y) for (x,y,c) in L]
	L_s.sort(reverse=True)

	s = 1
	t = 2

	p = {i:i for i in range(1, V+1)}

	m = -1
	for (c, x, y) in L_s:

		union(x, y)
		
		if(find(s) == find(t)):
			m=c
			break

	return m

import os
files = os.listdir("graphs/")
print(files)
c=0
for i in files:
	res = -1
	with open('graphs/' + i) as f:
		res = int(f.readline().split()[3])
	res_t = run('graphs/' + i)
	if(res == res_t):
		c+=1
		print(i + ": OK")
	else:
		print(i + ": answer is: " + str(res) + " found: " + str(res_t))
print(str(c) + "/" + str(len(files)))