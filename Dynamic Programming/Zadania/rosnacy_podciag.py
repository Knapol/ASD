def binary_search(sub, a):
    start = -1
    end = len(sub)-1
    while end - start > 1:
        s = start+(end - start)//2
        if sub[s] >= a:
            end = s
        else:
            start = s
    return end

# using sth different, however you can only get the length from this method, not the elements. Time complexity is far O(nlogn)
def find_seq(A):
    sub = []

    for a in A:
        if len(sub) == 0 or sub[-1] < a:
            sub.append(a)
        else:
            x = binary_search(sub, a)
            sub[x] = a
    return len(sub)


# using dynamic programming, complexity O(n^2), where n is the length of array
def find_sub_seq(A):
    n = len(A)
    dp = [0]*n

    for i in range(n):
        mn = 0
        for j in range(i-1,-1,-1):
            if A[j]<A[i]:
                mn = max(mn, dp[j])
        dp[i]=mn+1

    return max(dp)

A = [0,7,3,0,2,9]
B = [3,5,1,0,7,9]

print(find_seq(A))
print(find_seq(B))