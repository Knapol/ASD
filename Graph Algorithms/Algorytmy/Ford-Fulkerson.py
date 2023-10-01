from collections import deque
from copy import deepcopy

#bfs finds the path and return list of v
def bfs(graph, s, t):
    n = len(graph)
    parent = [None]*n
    path = []

    q = deque()
    q.append(s)
    parent[s] = -1

    while q:
        u = q.popleft()
        for v in range(n):
            if graph[u][v] == 1 and parent[v]==None:
                parent[v]=u
                q.append(v)
                if v == t:
                    index = t
                    path.append(t)
                    while parent[index]!=-1:
                        path.append(parent[index])
                        index = parent[index]
                    path.reverse()
                    break

    return path

def min_weight(graph, path):
    w = graph[path[0]][path[1]]
    for i in range(1, len(path)-1):
        w = min(graph[path[i]][path[i+1]], w)
    return w


def update_weights(graph, path):
    w = min_weight(graph, path)
    n = len(path)
    for i in range(n-1):
        graph[path[i]][path[i+1]] -= w
        graph[path[i+1]][path[i]] += w

def ford_fulkerson(graph, s, t):
    n = len(graph)
    counter = 0
    g = deepcopy(graph)

    path = bfs(graph, s, t)
    while path:
        counter += min_weight(g, path)
        update_weights(g, path)
        path = bfs(g, s, t)
    return counter

g = [
    [0,1,0,1,1],
    [1,0,0,1,0],
    [0,0,0,0,1],
    [1,1,0,0,1],
    [1,0,1,1,0]
]

#print(bfs(g,0,2))
print(ford_fulkerson(g,0,2))