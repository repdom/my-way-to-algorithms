edges = [map(int, x.split(' ')) for x in open('edges.txt', 'r').read().split('\n')[1:-1]]
vertex = set()
for edge in edges:
    vertex.add(edge[0])
    vertex.add(edge[1])
mst = set()
mst.add(vertex.pop())

total_cost = 0
while len(vertex)>0:
    best_cost = float("inf")
    for edge in edges:
        if edge[0] in mst and edge[1] in vertex and edge[2]<best_cost:
            best_cost = edge[2]
            best_vert = edge[1]
        if edge[1] in mst and edge[0] in vertex and edge[2]<best_cost:
            best_cost = edge[2]
            best_vert = edge[0]
    mst.add(best_vert)
    vertex.remove(best_vert)
    total_cost+=best_cost

print total_cost