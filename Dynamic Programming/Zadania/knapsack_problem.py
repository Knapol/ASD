inf = float('inf')

def knapsack(weights, values, max_w):
    n = len(weights)
    F = [[0 for _ in range(max_w+1)] for _ in range(n)]

    for b in range(weights[0], max_w+1):
        F[0][b]=values[0]
    
    for b in range(max_w+1):
        for i in range(1,n):
            F[i][b]=F[i-1][b]
            if b-weights[i]>=0:
                F[i][b]=max(F[i][b], F[i-1][b-weights[i]]+values[i])
    
    return F[n-1][max_w]

values = [10, 8, 4, 5, 3, 7]
weights = [4, 5, 7, 3, 1, 4]
max_w = 8

print(knapsack(weights, values, max_w))