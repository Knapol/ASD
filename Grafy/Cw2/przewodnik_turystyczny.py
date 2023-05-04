# Przewoźnik chce przewieźć grupę k turystów z miasta A do miasta B, między tymi miastami jest wiele miast, i 
# pomiędzy tymi miastami jeżdżą autobusy o różnej pojemności. Mamy Graf połączeń w postaci trójek [x,y,c], x-y miasta, c - pojemność autobusu na tej trasie.
# Przewodnik musi wyznaczyć wspólną trasę dla wszystkich turystów, musi w związku z tym ich podzielić na grupki tak, żeby każda grupka mogła przebyć trase bez rozdzielania się, 
# podaj algorytm który wylicza na ile grupek trzeba podzielić turystów (największa przepustowość ale bez Dijkstry żeby było śmiesznie

from collections import deque
from time import sleep

def BFS(graph, start, end, group):
    n = len(graph)
    visited = [False]*n
    q = deque()

    q.append(start)
    visited[start]=True

    while q:
        u = q.popleft()
        for v in graph[u]:
            if not visited[v[0]] and group <= v[1]:
                q.append(v[0])
                visited[v[0]]=True
                if v[0] == end:
                    return True
    return False

def get_max(g):
    maximum = 0
    for e in g:
        if e[2]>maximum:
            maximum = e[2]
    return maximum

def create_list(g, n):
    graph = [[] for _ in range(n)]
    for e in g:
        graph[e[0]].append((e[1],e[2]))
        graph[e[1]].append((e[0],e[2]))
    return graph

def how_many(g, start, end, n):
    maximum = get_max(g)

    graph = create_list(g, n)

    i = 1
    j = maximum
    best = None
    while i <= j:
        sleep(1)
        print(i,j)
        s = (i+j)//2
        if BFS(graph, start, end, s):
            best = s
            i=s+1
        else:
            j=s-1
    
    return best

A, B = 0, 9
n = 10

g = [
    [0,1,8],
    [1,2,6],
    [0,3,7],
    [3,2,9],
    [2,6,11],
    [0,4,10],
    [4,5,4],
    [5,6,3],
    [6,9,9],
    [4,7,11],
    [7,8,8],
    [8,9,8]
]

print(how_many(g, A, B, n))