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

	def __str__(self):
		return str(self.idx)

def print_sets_prev_next(sets):
	start = sets

	while(start.prev is not None):
		start = start.prev

	"""print('---------------------------------')
	while(start is not None):
		if(start.prev is not None):
			print(start.prev.vertices, end=' ')
		else:
			print(None, end = ' ')
		print(start.vertices, end = ' ')
		if(start.next is not None):
			print(start.next.vertices, end=' ')
		else:
			print(None, end = ' ')
		print()
		start = start.next
	print('---------------------------------')"""
	while(start is not None):
		print(start, ':', start.vertices, end = ' ')
		start = start.next
	print()

def print_sets_next_prev(sets):
	start = sets

	while(start.next is not None):
		start = start.next

	while(start is not None):
		print(start, ':', start.vertices, end = ' ')
		start = start.prev
	print()


def lexBSF(G, V, s=1):
	Vis = [False for _ in range(V+1)]

	v_to_set = dict()

	start_set = Set()
	start_set.vertices.add(s)
	v_to_set[s] = start_set

	vertices_set = Set()

	for i in range(1, V+1):
		if s == i:continue
		vertices_set.vertices.add(i)
		v_to_set[i] = vertices_set

	start_set.prev = vertices_set
	vertices_set.next = start_set

	current_set = start_set

	order = []

	while current_set is not None:

		u = current_set.vertices.pop()
		Vis[u] = True

		order.append(u)

		while not current_set.vertices:
			if(u == 7):
				print(current_set.vertices)

			current_set = current_set.prev
			if current_set is not None:
				current_set.next = None
			else:
				return order

		set_to_set = dict()

		for v in G[u]:
			if not Vis[v]:
				if v_to_set[v] not in set_to_set:
					curr = v_to_set[v]
					next = Set()

					next.next = curr.next
					curr.next = next
					next.prev = curr

					if next.next is not None:
						next.next.prev = next

					set_to_set[curr] = next

				v_to_set[v].vertices.remove(v)
				v_to_set[v] = set_to_set[v_to_set[v]]
				v_to_set[v].vertices.add(v)

		while current_set.next is not None:
			current_set = current_set.next

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
	G[8] = [2, 3, 4, 5, 7, 6]

	print(lexBSF(G, 8))
