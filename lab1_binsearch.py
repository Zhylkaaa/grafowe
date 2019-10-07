from dimacs import *

def solve(v, t, c):
	global Vis
	global neighbor_list

	if(Vis[v]):return False

	Vis[v] = True

	if(Vis[t]): return True

	for (i, c_t) in neighbor_list[v]:
		if(c_t >= c):
			if(solve(i,t,c)):return True

	return False


(V, L) = loadWeightedGraph("graphs/clique1000")


L_s = [(c, x, y) for (x,y,c) in L]
L_s.sort(reverse=True)

neighbor_list = [[] for i in range(V+1)]

for (x,y,c) in L:
	neighbor_list[x].append((y, c))
	neighbor_list[y].append((x, c))


s = 1
t = 2

l = 1
r = V

res = -1

while l<r:

	m = (l+r)//2

	c = L_s[m][0]
	res = c

	Vis = [False] * (V+1)

	if(solve(s, t, c)):
		r = m
	else:
		l = m+1

print(res)