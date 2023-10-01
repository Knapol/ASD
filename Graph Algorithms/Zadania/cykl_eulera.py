def dfs_visit(graph, u, path):
    
    for v in range(len(graph)):
        if graph[u][v]==1:
            graph[u][v] = graph[v][u] = 0
            dfs_visit(graph, v, path)
    path.insert(0, u)

def euler(graph):
    n = len(graph)
    total = 0
    for i in range(n):
        total += sum(graph[i])

        if total % 2 == 1:
            return False
        
    path = []
    dfs_visit(graph, 0, path)

    if len(path) != total//2+1:
        return False
    
    return path

g = [
    [0, 1, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 0]
]

print(euler(g))