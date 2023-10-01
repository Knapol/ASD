def f2(A, dp, i, l1, l2):
    if i > len(A)-1:
        return 0
    
    if dp[i][l1][l2] != -1:
        return dp[i][l1][l2]

    if A[i] > l1 and A[i] > l2:
        dp[i][l1][l2]=0
        return 0
    
    if A[i] > l1:
        dp[i][l1][l2] = f2(A, dp, i+1, l1, l2-A[i])+1
    elif A[i] > l2:
        dp[i][l1][l2] = f2(A, dp, i+1, l1-A[i], l2)+1
    else:
        dp[i][l1][l2] = max(f2(A, dp, i+1, l1, l2-A[i]), f2(A, dp, i+1, l1-A[i], l2))+1
    
    return dp[i][l1][l2]

def f(A, i, l1, l2, L):
    if i >= len(A):
        return 0

    if l1+A[i] > L and l2+A[i] > L:
        return 0

    return max(f(A, i+1, l1+A[i], l2, L)+1 if l1+A[i] <= L else 0, 
               f(A, i+1, l1, l2+A[i], L)+1 if l2+A[i] <= L else 0)

def prom_wyklad(A, L):
    return f(A, 0, 0, 0, L)

A = [4, 2, 1, 3]
L = 5

print(prom_wyklad(A, L))

dp = [[[-1 for _ in range(L+1)] for _ in range(L+1)] for _ in range(len(A))]
print(f2(A, dp, 0, L, L))