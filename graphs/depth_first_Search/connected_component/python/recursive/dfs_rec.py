def dfs_rec(graph,start,visited = []):
    visited.append(start)
    for v in graph[start]:
        if v not in visited:
            visited = dfs_rec(graph, v, visited)
    return visited

def test_algorithm():
	graph = {'A':['B','C'],'B':['D','E'],'C':['D','E'],'D':['E'],'E':['A']}
	print dfs_rec(graph, 'A')

test_algorithm()