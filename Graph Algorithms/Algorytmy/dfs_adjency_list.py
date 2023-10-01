def dfs_visit(graph, u, visited, parent):
    visited[u]= True

    for v in graph[u]:
        if not visited[v]:
            parent[v]=u
            dfs_visit(graph, v, visited, parent)

def dfs(graph, s):
    visited = [False]*len(graph)
    parent = [None]*len(graph)

    for u in range(len(graph)):
        if visited[u] == False:
            parent[u] = -1
            dfs_visit(graph, u, visited, parent)

    return parent

graph = [[1, 8], [0], [3, 4, 5, 8], [2], [2, 7], [2, 6], [5, 8], [4, 6], [0, 2, 6], [10], [9]]
print(dfs(graph, 0))