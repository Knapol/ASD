def convert(num):
    tmp = num
    tab = [0]*10
    while tmp > 0:
        tab[tmp%10]+=1
        tmp //= 10
    
    single = 0
    multiple = 0

    for i in range(10):
        if tab[i] == 1:
            single+=1
        if tab[i] > 1:
            multiple+=1
    
    return (num, single, multiple)

def counting_sort(A, k, index):
    n = len(A)
    C = [0]*k
    B = [0]*n
    for i in range(n):
        C[A[i][index]]+=1

    for i in range(1, k):
        C[i]=C[i]+C[i-1]

    for i in range(n-1, -1, -1):
        B[C[A[i][index]]-1]=A[i]
        C[A[i][index]]-=1

    if index == 2:
        for i in range(n):
            A[i]=B[n-i-1]
    else:
        for i in range(n):
            A[i]=B[i]

def pretty_sort(T):
    d = len(T)
    for i in range(d):
        T[i]=convert(T[i])
    print(T)
    counting_sort(T, 10, 2)
    counting_sort(T, 10, 1)

    for i in range(d):
        T[i]=T[i][0]

    return T

T = [123, 455, 1266, 114577, 2344, 6733]
print(pretty_sort(T))