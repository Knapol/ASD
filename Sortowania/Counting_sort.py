#Mamy tablicę A, która zawiera liczby naturalnez zakresu {0,1,...,k-1}

def counting_sort(A, k):
    n = len(A)
    C = [0]*k
    B = [0]*n

    for i in range(n):
        C[A[i]] += 1

    for i in range(1, k):
        C[i]=C[i]+C[i-1]
    
    for i in range(n-1, -1, -1):
        B[C[A[i]]-1]=A[i]
        C[A[i]]-=1
    
    for i in range(n):
        A[i]=B[i]

tab = [5,3,6,3,7,2,7,3,7,2,3,7,2,1,6,3,8,5,9,4,7,5,9]

counting_sort(tab, 10)

print(tab)