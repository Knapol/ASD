#O(E*log(V))
#O(V^2) macierz
from queue import PriorityQueue

inf = float('inf')

def relax(u, v, distance, parent):
    if distance[v[0]] > distance[u]+v[1]:
        distance[v[0]] = distance[u]+v[1]
        parent[v[0]] = u
        return True
    return False

def dijkstra2(graph, s):
    q = PriorityQueue()
    n = len(graph)
    parent = [None]*n
    distance = [inf]*n
    visited = [False]*n

    q.put((0, s))
    distance[s]=0
    parent[s]=-1
    
    while not q.empty():
        dist, u = q.get()
        for v in graph[u]:
            # print(distance)
            if not visited[v[0]] and relax(u, v, distance, parent):
                q.put((dist+v[1], v[0]))
        visited[u] = True
    return distance, parent

def dijkstra(graph, s):
    n = len(graph)
    dist = [inf for _ in range(n)]
    parent = [None]*n
    q = PriorityQueue()

    q.put((0, s, -1))

    while not q.empty():
        d, u, p = q.get()
        if dist[u] == inf:
            dist[u]=d
            parent[u]=p
            for v in graph[u]:
                if dist[v[0]]==inf:
                    q.put((v[1]+d,v[0], u))
    return dist, parent

def dijkstra3(graph, s):
    n = len(graph)
    d = [inf for _ in range(n)]
    parent = [None]*n
    q = PriorityQueue()

    q.put((0, s, -1))

    while not q.empty():
        distance, u, p = q. get()
        if d[u] == inf:
            d[u] = distance
            parent[u] = p
            for (v,w) in graph[u]:
                if d[v] == inf:
                    q.put((d[u]+w, v, u))
    return d, parent

graph = [[(1, 1), (2, 12)],
         [(0, 1), (2, 7), (3, 5)],
         [(0, 12), (1, 7), (3, 6), (4, 2)],
         [(1, 5), (2, 6), (4, 5), (5, 100)],
         [(2, 2), (3, 5), (5, 9)],
         [(3, 100), (4, 9)]]

print(dijkstra(graph, 0))
print(dijkstra2(graph, 0))
print(dijkstra3(graph, 0))