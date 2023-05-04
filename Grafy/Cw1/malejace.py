# graf gdzie każda krawędź ma wartość i musisz przejść z A do B po coraz mniejszych co do wartości krawędziach; BFS tylko zamiast visited sprawdzasz wartość krawędzi

from collections import deque

inf = float('inf')

def BFS(graph, A, B):
    n = len(graph)
    visited = [False]*n
    q = deque()
    q.append((A, inf))
    visited[A]=True

    while q:
        u, w = q.popleft()
        for v in graph[u]:
            if w > v[1]:
                q.append(v)
                if v[0] == B:
                    return True
                
    return False

g = [
    [(1,9),(4,1)],
    [(0,9),(2,4),(5, 8),(6,8)],
    [(1,4),(3,3),(5,2)],
    [(2,3),(4,2),(5,8)],
    [(0,1),(3,2),(5,9)],
    [(1,8),(2,2),(4,9),(8,8)],
    [(1,8),(7,7)],
    [(6,7)],
    [(5,8)]
]

print(BFS(g, 0, 8))