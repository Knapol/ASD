def DFS_visit(graph, u, visited, parent,result):
    visited[u] = True
    result.append(u)
    for v in graph[u]:
        if not visited[v]:
            visited[v]=True
            parent[v]=u
            DFS_visit(graph, v, visited, parent, result)

def DFS(graph):
    n = len(graph)
    visited = [False]*n
    parent = [-1]*n
    result = []
    
    for u in range(len(graph)):
        if not visited[u]:
            DFS_visit(graph, u, visited, parent, result)

    return parent, result

g = [
    [1,4],
    [0,2,5,6],
    [1,3,5],
    [2,4,5],
    [0,3,5],
    [1,2,4,8],
    [1,7],
    [6],
    [5]
]

print(DFS(g))