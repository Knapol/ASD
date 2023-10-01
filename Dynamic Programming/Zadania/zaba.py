inf = float('inf')

def zaba(A):
    n = len(A)

    dp = [inf for _ in range(n)]
    dp[0]=(A[0],0)

    for i in range(n):
        curr_energy, moves = dp[i]
        for j in range(1, curr_energy+1):
            if i+j > n-1:
                break
            if dp[i+j] == inf:
                dp[i+j] = (curr_energy-j+A[i+j], moves+1)
            else:
                if dp[i+j][1] > moves+1:
                    dp[i+j] = (curr_energy-j+A[i+j], moves+1)
                    
    return dp[n-1][1]

A = [4, 5, 2, 2, 6, 8, 47, 1, 4, 1, 2, 0]
B = [3, 1, 2, 0, 0, 2, 0]
print(zaba(A))
print(zaba(B))