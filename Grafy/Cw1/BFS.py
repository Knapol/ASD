from collections import deque

def BFS(graph, start):
    n = len(graph)
    visited = [False]*n
    q = deque()
    q.append(start)

    result = [0]*n
    visited[0]=True

    counter=1
    while q:
        u = q.popleft()
        result[u]=counter
        counter+=1
        for v in graph[u]:
            if not visited[v]:
                q.append(v)
                visited[v]=True
    return result

g = [
    [1,4],
    [0,2,5],
    [1,3,5],
    [2,4,5],
    [0,3,5],
    [1,2,4]
]

print(BFS(g, 0))