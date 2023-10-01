# ścieżka Hamiltona w dag-u; lista sąsiedztwa

def DFS_visit(graph, u, visited, top_sort):
    visited[u]=True
    for v in graph[u]:
        if not visited[v]:
            DFS_visit(graph, v, visited, top_sort)

    top_sort.append(u)

def DFS(graph):
    top_sort = []
    visited = [False]*len(graph)

    for u in range(len(graph)):
        if not visited[u]:
            DFS_visit(graph, u, visited, top_sort)

    return top_sort

def contains(graph, v1, v2):
    for v in graph[v1]:
        if v == v2:
            return True
    return False

def hamilton(graph):
    top_sort = DFS(graph)
    top_sort.reverse()
    print(top_sort)
    for i in range(1,len(top_sort)):
        if not contains(graph, top_sort[i-1], top_sort[i]):
            return False
    return True

g = [
    [4],
    [5,7],
    [1],
    [2],
    [3],
    [6],
    [],
    []
]

print(hamilton(g))
