currentLabel = 0
f = {}

def DFS_Loop(graph):
    checked = []
    global currentLabel
    currentLabel = len(graph)
    for edge in graph.keys():
        if edge not in checked :
            checked = DFS(graph,edge, checked)

def DFS(graph, start, path=[]):
    path = path + [start]
    global currentLabel
    global f
    for edge in graph[start]:
        if edge not in path:
            path = DFS(graph, edge, path)

    f[currentLabel] =  start
    currentLabel = currentLabel - 1
    return path

# graph = {
#     1: [2,11],
#     2: [3],
#     11: [12],
#     12: [13],
#     3: [],
#     13:[]
#     }
graph = {'A':['B','C'],'B':['D'],'C':['D'], 'D':['H','J'], 'H':['O'], 'J':['I'], 'O':['P'], 'P':[], 'I':[]}
DFS_Loop(graph)
print f