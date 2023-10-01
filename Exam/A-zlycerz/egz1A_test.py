# Bartosz Knapik
# Algorytm polega na zastosowaniu algorytmu dijkstry. Algorytm dijkstry znajduje najkrotsza sciezke w grafie (w tym wypadku
# tę z najwiekszym zyskiem/najmniejsza strata). Aby algorytm działał kazdy wierzcholek duplikuje (tzn tablica distance -
# przechowujaca najtansze koszty, przechowuje dla kazdego wierzcholka tablice dwuelementowa) to znaczy najwiekszy zysk
# gdy rycerz nie napadł na zamek, i gdy rycerz napadl na zamek. Dzieki temu sledze osobno dwa przypadki i na koncu moge zwrocic
# minimum z kosztow dotarcia do koncowego wierzcholka tzn min(koszt z napadem, bez napadu)
# dzieki takiej tablicy distance, mam pewnosc ze algorytm dijkstry zadziala poprawnie

# zlozonosc mojego algorytmu to zlozonosc algorytmu dijkstry, zatem O(V^2*log(V))

from egz1Atesty import runtests

from queue import PriorityQueue

inf = float('inf')

def dijkstra(graph, castles, s, t, r):
  n = len(graph)
  q = PriorityQueue()
  distance = [[inf, inf] for _ in range(n)]
  
  # krotka postaci (koszt, wierzcholek, czy byl napad)
  # jesli 0 to napadu nie bylo, jesli 1 to napad byl
  q.put((0, s, 0))
  q.put((-castles[s], s, 1))
  distance[s][0] = 0
  distance[s][1] = -castles[s]

  while not q.empty():
    cost, u, flag = q.get()
    for v in graph[u]:

      if flag == 0:
          if distance[v[0]][flag] > distance[u][flag]+v[1]:
            distance[v[0]][flag] = distance[u][flag]+v[1]
            q.put((distance[v[0]][flag], v[0], 0))

            if distance[v[0]][1] > distance[v[0]][flag]-castles[v[0]]:
               q.put((distance[v[0]][flag]-castles[v[0]], v[0], 1))
               distance[v[0]][1] = distance[v[0]][flag] - castles[v[0]]
      if flag == 1:
          if distance[v[0]][flag] > distance[u][flag]+2*v[1]+r:
            distance[v[0]][flag] = distance[u][flag]+2*v[1]+r
            q.put((distance[v[0]][flag], v[0], 1))
  return min(distance[t][0], distance[t][1])

def gold(G,V,s,t,r):
  return dijkstra(G, V, s, t, r)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
