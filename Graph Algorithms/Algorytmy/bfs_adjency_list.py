from collections import deque

def bfs(graph, s):
    visited = [False]*len(graph)
    parent = [None]*len(graph)
    q = deque()

    q.append(s)
    visited[s]=True
    parent[s]=-1
    
    for i in range(len(graph)):
        while q:
            u = q.popleft()
            for v in graph[u]:
                if visited[v] == False:
                    visited[v]=True
                    parent[v]=u
                    q.append(v)
        if visited[i] == False:
            q.append(i)
            parent[i]=-1
            visited[i]=True
    return parent

graph = [[1, 8], [0], [3, 4, 5, 8], [2], [2, 7], [2, 6], [5, 8], [4, 6], [0, 2, 6], [10], [9]]
print(bfs(graph, 0))