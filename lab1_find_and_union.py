from dimacs import *

def union(x, y):
	global p
	a= p[x]
	b=p[y]

	p[a] = b

def find(x):
	global p
	if(p[x] != x):
		v = p[x]
		p[x]=find(v)
		return p[x]
	else:
		return x

(V, L) = loadWeightedGraph("graphs/g1")


L_s = [(c, x, y) for (x,y,c) in L]
L_s.sort(reverse=True)

s = 1
t = 2

p = [i for i in range(V+1)] 

m = -1
for (c, x, y) in L_s:

	union(x, y)
	m = c
	if(find(s) == find(t)):
		break

print(m)