def bfs_iter(graph, start, visited=[]):
	queue=[start]
	while queue:
		v = queue.pop(0) # FIFO
		if v not in visited:
			visited.append(v)
			queue.extend(graph[v])
	return visited

def test_algorithm():
	graph = {'A':['B','C'],'B':['D','E'],'C':['D','E'],'D':['E'],'E':['A']}
	print bfs_iter(graph, 'A')

test_algorithm()