def knapsack(P, W, H):
    n = len(P) # ilosc przedmiotow

    dp = [ [ [0 for _ in range(H+1) ] for _ in range(W+1) ] for _ in range(n)]

    for i in range(n):
        for w in range(W+1):
            for h in range(H+1):
                value = P[i][0]
                weight = P[i][1]
                height = P[i][2]
                dp[i][w][h] = dp[i-1][w][h]
                if w-weight >= 0 and h-height >= 0:
                    dp[i][w][h] = max(dp[i][w][h], dp[i-1][w-weight][h-height]+value)
    return dp[-1][-1][-1]

P = [(10, 4, 2), (8, 5, 3), (4, 12, 1), (5, 9, 7), (3, 1, 4), (7, 13, 4)]
# (value, weight, height)
W = 24
H = 9
print(knapsack(P, W, H))