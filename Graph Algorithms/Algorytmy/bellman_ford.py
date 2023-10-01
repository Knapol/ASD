# O(VE)
inf = float('inf')

def relax(u, v, distance, parent):
    if distance[v[0]] > distance[u]+v[1]:
        distance[v[0]] = distance[u]+v[1]
        parent[v[0]] = u

def bellman_ford(graph, s):
    n = len(graph)
    V = n

    distance = [inf]*n
    parent = [None]*n

    distance[s]=0

    for i in range(V-1):
        for u in range(n):
            for v in graph[u]:
                relax(u, v, distance, parent)
    
    for u in range(n):
        for v in graph[u]:
            if distance[v[0]] > distance[u]+v[1]:
                return False, None, None
                
    return True, distance, parent

graph1 = [[(1, 1), (2, 12)],
         [(0, 1), (2, 7), (3, 5)],
         [(0, 12), (1, 7), (3, 6), (4, 2)],
         [(1, 5), (2, 6), (4, 5), (5, 100)],
         [(2, 2), (3, 5), (5, 9)],
         [(3, 100), (4, 9)]]

g = [[0, 1, 6], [0, 2, 7], [1, 2, 8], [1, 3, 5], [1, 4, -4], [2, 3, -3],
         [2, 4, 9], [3, 1, -2], [4, 0, 2], [4, 3, 7]]

max1 = 0
for e in g:
    if e[0]>max1:
        max1 = e[0]
    if e[1]>max1:
        max1 = e[1]

new_graph = [[] for _ in range(max1+1)]
for e in g:
    new_graph[e[0]].append([e[1],e[2]])

print(new_graph)

result, distance, parent = bellman_ford(new_graph, 0)

print(result, distance, parent)


                