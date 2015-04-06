import collections

Edge = collections.namedtuple('Edge', ['vertice1', 'vertice2', 'cost'])
Graph = collections.namedtuple('Graph', ['edges', 'vertices'])

parent = dict()
rank = dict()

def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1

def clustering(min_clusters, graph):

    initial_cluster = len(graph.vertices)
    max_spacing = 0
    for vertice in graph.vertices:
        make_set(vertice)

    edges = sorted(graph.edges, key=lambda e: e.cost)

    while initial_cluster => min_clusters:
        edge = edges.pop(0)
        vertice1, vertice2, weight = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            initial_cluster = initial_cluster - 1
            max_spacing = weight
    return max_spacing

def read_graph(filename):
    edges = []
    vertices = set()
    with open(filename) as f:
        n_of_edges = f.readline()
        for line in f:
            v1, v2, cost = line.split(' ')
            edges.append(Edge(v1, v2, int(cost)))
            vertices.add(v1)
            vertices.add(v2)
    return Graph(edges, vertices)


def main ():
    graph = read_graph('clustering1.txt')
    spacing = clustering(4, graph)
    print spacing


if __name__ == "__main__":
    print main()