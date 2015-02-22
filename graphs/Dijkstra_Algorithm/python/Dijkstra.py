from heapq import heappush, heappop

def main(fileName):
    G = {}
    with open(fileName,"r") as f:
        for line in f:
            G[int(line.split()[0])] = {(int(tup.split(",")[0])): int(tup.split(",")[1]) for tup in line.split()[1:] if tup}

    f.close()

    endList = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    for i in range(len(endList)):
        D, _ = dijkstra(G, 1, endList[i])
        endList[i] = (endList[i], D[endList[i]])

    print findshortestPath(G, 1, 114)

    return endList


def dijkstra(G, start, end = None):
    distance = {vertex: float("inf") for vertex in G}
    path = {vertex: None for vertex in G}
    queue = [(0, start)]
    visited = set()

    distance[start] = 0

    while queue:
        _, vertex = heappop(queue)
        if vertex in visited: continue

        visited.add(vertex)
        if vertex == end: break

        for w in G[vertex]:
            vwLength = distance[vertex] + G[vertex][w]
            if vwLength < distance[w]:
                distance[w], path[w] = vwLength, vertex

            heappush(queue, (distance[w], w))

    return distance, path

def findshortestPath(G, start, end):
    _, P = dijkstra(G, start, end)
    path = []
    while True:
        path.insert(0, end)
        if end == start: break
        end = P[end]

    #path.reverse()
    return path

if __name__ == "__main__":
    print main("dijkstraData.txt")