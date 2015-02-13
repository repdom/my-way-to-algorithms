def edgesToAdjacency(edges):
    graph = {}
    for i, edge in edges.iteritems():
        graph.setdefault(edge[0], []).append(edge[1])
    return graph


print edgesToAdjacency({1:(1,2),2:(1,3),3:(2,4),4:(3,5)})