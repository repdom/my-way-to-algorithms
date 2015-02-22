def initialize(graph, source):
	destination = {vertex: float("inf") for vertex in graph}
	predecessor = {vertex: None for vertex in graph}
	destination[source] = 0

	return destination, predecessor

def relaxation(vertex, neighbour, graph, destination, predecessor):
	if destination[neighbour] > destination[vertex] + graph[vertex][neighbour]:
		destination[neighbour] = destination[vertex] + graph[vertex][neighbour]
		predecessor[neighbour] = vertex

def bellman_ford(graph, source):
	destination, predecessor = initialize(graph, source)
	for i in range(len(graph) -1):
		for vertex in graph:
			for neighbour in graph[vertex]:
				relaxation(vertex, neighbour, graph, destination, predecessor)

	#check for negative-weight cycles
	for vertex in graph:
		for neighbour in graph[vertex]:
			if destination[neighbour] > destination[vertex] + graph[vertex][neighbour]:
				raise ValueError('negative cycle')

	return destination, predecessor

def test():
	graph = {
		'a': {'b': -1, 'c':  4},
		'b': {'c':  3, 'd':  2, 'e':  2},
		'c': {},
		'd': {'b':  1, 'c':  5},
		'e': {'d': -3}
		}

	d, p = bellman_ford(graph, 'a')

	assert d == {
		'a':  0,
		'b': -1,
		'c':  2,
		'd': -2,
		'e':  1
		}

	assert p == {
		'a': None,
		'b': 'a',
		'c': 'b',
		'd': 'e',
		'e': 'b'
		}

if __name__ == '__main__': test()