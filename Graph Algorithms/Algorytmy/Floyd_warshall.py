# O(V^3)
inf = float('inf')

def floyd_warshall(graph):
    n = len(graph)

    distance = [[inf for _ in range(n)] for _ in range(n)]

    for u in range(n):
        for v in range(n):
            if u == v:
                distance[u][v]=0
            elif graph[u][v] != inf:
                distance[u][v] = graph[u][v]

    for dist in distance:
        print(dist)

    for i in range(n):
        for u in range(n):
            for v in range(n):
                distance[u][v] = min(distance[u][v], distance[u][i]+distance[i][v])
    
    return distance

def minimal_wage_cycle(graph):
    n = len(graph)
    distance = floyd_warshall(graph)
    ans = inf
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            ans = min(ans, distance[i][j]+distance[j][i])

    for dist in distance:
        print(dist)
    print(ans)
    return

g = [
    [0,  inf,0,  inf,inf],
    [9,  0,  inf,inf,inf],
    [inf,0,  0,  inf,3],
    [inf,inf,1,  0,  inf],
    [inf,inf,inf,2,  0]
]

minimal_wage_cycle(g)