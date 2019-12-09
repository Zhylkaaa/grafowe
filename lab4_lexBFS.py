from queue import Queue

class Set:
	counter = 0

	def __init__(self):
		self.idx = Set.counter
		Set.counter += 1
		self.vertices = set()
		self.next = None
		self.prev = None

	def __hash__(self):
		return hash(self.idx)

def lexBSF(G, V, s=1):
	Vis = [False for _ in range(V+1)]

	order = []

	Sets = Set()

	for v in range(1, V+1):
		Sets.vertices.add(v)	

	v_to_set = {v: Sets for v in range(1, V+1)}

	while Sets is not None:
		if Vis[s] == False:
			v = s 
			Sets.vertices.remove(s)
		else:
			v = Sets.vertices.pop()

		order.append(v)

		if not Sets.vertices:
			Sets = Sets.prev
			if Sets is not None:
				Sets.next = None

		if Sets is None:
			break

		Vis[v] = True

		set_to_set = dict()

		for u in G[v]:
			if not Vis[u]:
				if v_to_set[u] not in set_to_set:
					set_to_set[ v_to_set[u] ] = Set()
					set_to_set[ v_to_set[u] ].next = v_to_set[u].next
					v_to_set[u].next = set_to_set[ v_to_set[u] ]
					set_to_set[ v_to_set[u] ].prev = v_to_set[u]

				set_to_set[ v_to_set[u] ].vertices.add(u)
				v_to_set[u].vertices.remove(u)

				if not v_to_set[u].vertices:
					if v_to_set[u].prev is not None and v_to_set[u].next is not None:
						v_to_set[u].prev.next = v_to_set[u].next
						v_to_set[u].next.prev = v_to_set[u].prev
					elif v_to_set[u].prev is None:
						v_to_set[u].next.prev = None
					elif v_to_set[u].next is None:
						v_to_set[u].prev.next = None

				v_to_set[u] = set_to_set[ v_to_set[u] ]

		while Sets.next is not None:
			Sets = Sets.next

	return order

if __name__ == '__main__':
	G = [[] for _ in range(9)]
	G[1] = [6]
	G[2] = [8]
	G[3] = [6, 8]
	G[4] = [8, 7]
	G[5] = [8, 7]
	G[6] = [7, 3, 1, 8]
	G[7] = [4, 5, 6, 8]
	G[8] = [2, 3, 5, 7, 6]

	print(lexBSF(G, 8))
