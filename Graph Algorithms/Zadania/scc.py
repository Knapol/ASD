def change_direction(graph):
    n = len(graph)
    new_graph = [[] for _ in range(n)]

    for u in range(n):
        for v in graph[u]:
            new_graph[v].append(u)

    return new_graph

def dfs_first(graph, u, visited, stack):
    visited[u] = True
    
    for v in graph[u]:
        if not visited[v]:
            dfs_first(graph, v, visited, stack)

    stack.append(u)

    

def dfs_visit(graph, u, visited, skladowe, index):
    visited[u] = True
    skladowe[index].append(u)
    for v in graph[u]:
        if not visited[v]:
            dfs_visit(graph, v, visited, skladowe, index)
    

def scc(graph):
    n = len(graph)
    index = 0
    visited = [False]*n
    stack = []
    skladowe = [[] for _ in range(n)]

    for u in range(len(graph)):
        if not visited[u]:
            dfs_first(graph, u, visited, stack)

    visited = [False]*n
    g = change_direction(graph)
    stack.reverse()
    for u in stack:
        if not visited[u]:
            index+=1
            dfs_visit(g, u, visited, skladowe, index)

    return skladowe

graph = [[1, 4], [2, 3], [0, 7], [4], [5], [3, 6], [3], [8], [9], [10], [6, 7]]
""" graph = [
    [1],
    [2],
    [0,3],
    [4],
    [5],
    [6],
    [4]
] """
print(scc(graph))