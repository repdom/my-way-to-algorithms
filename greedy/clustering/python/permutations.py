from bitarray import bitarray

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

def read_graph(filename):
    nodes = set()
    with open(filename) as f:
        n_of_nodes = f.readline()
        for line in f:
            nodes.add(line.strip().replace(" ", ""))
    return nodes

def bitmasks(n,m):
    if m < n:
        if m > 0:
            for x in bitmasks(n-1,m-1):
                yield bitarray([1]) + x
            for x in bitmasks(n-1,m):
                yield bitarray([0]) + x
        else:
            yield n * bitarray('0')
    else:
        yield n * bitarray('1')

def clustering(nodes):

    initial_cluster = len(nodes)

    for node in nodes:
        make_set(node)

    def compute_unions(elements, groups):
        for b in bitmasks(elements,groups):
            z = b^bitarray(x)
            if z.to01() in nodes:
                if find(z.to01() ) != find(x):
                    union(z.to01() , x)
                    initial_cluster = initial_cluster - 1
                    continue

    for x in nodes:
        compute_unions(24,1)
        compute_unions(24,2)
    return initial_cluster

nodes = read_graph('clustering_big.txt')
print clustering(nodes)