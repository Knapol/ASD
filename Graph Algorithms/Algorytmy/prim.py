# O(Elog(V))
from queue import PriorityQueue

inf = float('inf')

def prim(graph, s):
    n = len(graph)
    q = PriorityQueue()
    visited = [False]*n
    key = [inf]*n
    parent = [None]*n
    
    q.put((0, s))
    visited[s]=True
    key[s]=0

    while not q.empty():
        dist, u = q.get()
        visited[u]=True
        
        for v in graph[u]:
            if key[v[0]] > v[1] and not visited[v[0]]:
                parent[v[0]]=u
                key[v[0]]=v[1]
                q.put((key[v[0]], v[0]))
    result = []

    for i in range(n):
        if parent[i] != None:
            result.append((i, parent[i], key[i]))
    return result

graph = [[(1, 7), (2, 8), (3, 3), (4, 2)],
         [(0, 7), (2, 1)],
         [(0, 8), (1, 1), (3, 12), (5, 4)],
         [(0, 3), (2, 12), (5, 6)],
         [(0, 2), (5, 5)],
         [(2, 4), (3, 6), (4, 5)]]

print(prim(graph, 0))
