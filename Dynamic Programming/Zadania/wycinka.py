def black_forest(T):
    n = len(T)
    dp = [0 for _ in range(n)]

    dp[0]=T[0]
    dp[1]=max(T[0], T[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2]+T[i])
    
    return dp[n-1]


T = [5,2,5,6,3,6,12,6,3,3,73,12]

print(black_forest(T))