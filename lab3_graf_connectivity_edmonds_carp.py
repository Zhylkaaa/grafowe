from dimacs import loadDirectedWeightedGraph
from lab2_edmonds_carp import edmonds_carp

def run(file_name):
	V, L = loadDirectedWeightedGraph(file_name)
	L_b = L.copy()

	for (x,y,w) in L:
		L_b.append((y,x,w))

	res = 10000000000

	for i in range(1, V+1):
		for j in range(1, V+1):
			if i == j:continue
			res = min(res, edmonds_carp(L_b, V, i, j))

	return res

import time 
import os
files = os.listdir("graphs-lab3/")
print(files)
c=0

for i in files:
	if(i in ['grid100x100', 'clique200', 'clique100']):
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

#run('graphs-lab3/trivial')