#O(Elog(V))

class Node:
    def __init__(self, value):
        self.value = value
        self.rank = 0
        self.parent = self
    
def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank+=1

def convert_to_edges(graph):
    edges = []
    n = len(graph)
    for u in range(n):
        for v in graph[u]:
            if (v[0], u, v[1]) not in edges: 
                edges.append((u, v[0], v[1]))
    return edges

def kruskal(graph):
    n = len(graph)
    edges = convert_to_edges(graph)
    edges.sort(key = lambda x: x[2])
    MST = []
    V = []

    for i in range(n):
        V.append(Node(i))

    for i in range(n):
        u = edges[i][0]
        v = edges[i][1]
        if find(V[u]) != find(V[v]):
            MST.append(edges[i])
            union(V[u], V[v])
    return MST


graph = [[(1, 7), (2, 8), (3, 3), (4, 2)],
         [(0, 7), (2, 1)],
         [(0, 8), (1, 1), (3, 12), (5, 4)],
         [(0, 3), (2, 12), (5, 6)],
         [(0, 2), (5, 5)],
         [(2, 4), (3, 6), (4, 5)]]

print(kruskal(graph))