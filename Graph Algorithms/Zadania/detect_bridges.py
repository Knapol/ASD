inf = float('inf')
    
def bridge(graph):
    n = len(graph)
    visited = [False]*n
    time_visit = [0]*n
    low = [inf]*n
    parent = [None]*n
    time = 0

    def dfs_visit(graph, u, visited, parent, time_visit, low):
        nonlocal time
        visited[u] = True
        time_visit[u] = time
        time+=1
        low[u]=time_visit[u]
        for v in graph[u]:
            if not visited[v]:
                parent[v]=u
                dfs_visit(graph, v, visited, parent, time_visit, low)
                low[u]=min(low[u], low[v])
            elif parent[u] != v:
                low[u]=min(low[u], time_visit[v])

    for i in range(n):
        if not visited[i]:
            dfs_visit(graph, i, visited, parent, time_visit, low)

    print(time_visit, low, parent)

    for i in range(n):
        if time_visit[i]==low[i] and parent[i] != None:
            print(parent[i], i)

#graph = [[1, 4], [0, 2], [1, 3, 4], [2, 5, 6], [0, 2], [3, 6], [3, 5, 7], [6]]
""" graph = [
    [1,6],
    [0,2],
    [1,3,6],
    [2,4,5],
    [3,5],
    [3,4],
    [0,2,7],
    [6]
] """

graph = [
    [1, 2],
    [0,2,3],
    [0,1],
    [1]
]

bridge(graph)