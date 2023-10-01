# Bartosz Knapik 
# Algorytm polega na rekurencji z memoizacją. Dla kazdej odwiedzonej planety, badam do jakich planet mozna dotrzec (i z jakim
# kosztem), (rozwazam przypadki z teleportacja oraz bez). W tablicy o nazwie dp (sluzacej do przechowywania obliczonych juz
# wartosci trzymam minimalne koszty dotarcia do planety z okreslona iloscia paliwa). Jesli nie bylem w danej planecie lub
# moge sie w niej teraz znalezc mniejszym kosztem, ale przy tej samej ilosci paliwa to wchodzę głebiej rekurencją
# rekurencja konczy sie po rozwazeniu wszystkich sposobow na dotarcie do wierzcholka n-1
# nie rozwazam przypadku polecenia najpierw na dalszą planete od startu, a z niej na planete blizszą startu, gdyż taki koszt 
# bedzie zawsze wiekszy
# Zloznosc algorytmu to zloznosc wielomianowa wzgledem n i E, O(n*E^2)

from egz1btesty import runtests

inf = float('inf')

def planets( D, C, T, E ):
    min_cost = inf

    n = len(D)
    dp = [[None for _ in range(E+1)] for _ in range(n)]

    def rek(D, C, T, E, fuel, i, cost, dist, dp):
        nonlocal min_cost
        n = len(D)
        if i == n-1:
            min_cost = min(min_cost, cost)
            return
        
        # uzycie teleportacji
        if fuel == 0:
            if T[i][0] != i:
                if dp[T[i][0]][0] == None or dp[T[i][0]][0] > cost+T[i][1]:
                    rek(D, C, T, E, 0, T[i][0], cost+T[i][1], D[T[i][0]], dp)
        
        curr_cost = cost
        curr_fuel = fuel
        # dla kazdej ilosci paliwa sprawdzam do jakich planet mozna poleciec
        while curr_fuel <= E:
            for j in range(i+1, n):
                distance = D[j]-dist
                if curr_fuel >= distance:
                    if dp[j][curr_fuel-distance] == None or dp[j][curr_fuel-distance] > curr_cost:
                        dp[j][curr_fuel-distance] = curr_cost
                        rek(D, C, T, E, curr_fuel-distance, j, curr_cost, D[j], dp)
            curr_fuel += 1
            curr_cost += C[i]

    rek(D, C, T, E, 0, 0, 0, 0, dp)

    return min_cost

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
