def dfs_visit(graph, u, visited, parent):
    visited[u]=True
    for v in range(len(graph)):
        if graph[u][v]==1 and not visited[v]:
            parent[v]=u
            dfs_visit(graph, v, visited, parent)

def dfs(graph, s):
    visited = [False]*len(graph)
    parent = [None]*len(graph)
    
    for u in range(len(graph)):
        if not visited[u]:
            parent[u]=-1
            dfs_visit(graph, u, visited, parent)

    return parent

graph = [[0, 1, 0, 1, 1],
         [1, 0, 0, 1, 0],
         [0, 0, 0, 0, 1],
         [1, 1, 0, 0, 1],
         [1, 0, 1, 1, 0]]

print(dfs(graph, 0))