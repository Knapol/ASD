from collections import deque

def bfs(graph, s):
    visited = [False]*len(graph)
    parent = [None]*len(graph)
    q = deque()
    
    q.append(s)
    visited[s]=True
    parent[s]=-1

    while q:
        u = q.popleft()
        for v in range(len(graph)):
            if graph[u][v] == 1 and visited[v] == False:
                visited[v]=True
                parent[v]=u
                q.append(v)
    return parent

graph = [[0, 1, 0, 1, 1],
         [1, 0, 0, 1, 0],
         [0, 0, 0, 0, 1],
         [1, 1, 0, 0, 1],
         [1, 0, 1, 1, 0]]

print(bfs(graph, 0))