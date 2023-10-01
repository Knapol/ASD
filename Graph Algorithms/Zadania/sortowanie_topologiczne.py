def dfs_visit(graph, u, visited, parent, after_sort):
    visited[u] = True
    
    for v in graph[u]:
        if not visited[v]:
            parent[v]=u
            dfs_visit(graph, v, visited, parent, after_sort)
    after_sort.insert(0, u)
    
def dfs(graph):
    visited = [False]*len(graph)
    parent = [None]*len(graph)

    after_sort = []

    for i in range(len(graph)):
        if not visited[i]:
            dfs_visit(graph, i, visited, parent, after_sort)
    
    return after_sort

graph = [[1, 2], [2, 3], [], [4, 5, 6], [], [], [], [3], [7]]

print(dfs(graph))