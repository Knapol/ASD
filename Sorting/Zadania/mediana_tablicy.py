# Dana jest dwuwymiarowa tablica T o rozmiarach N × N wypełniona liczbami naturalnymi (liczby
# są parami różne). Proszę zaimplementować funkcję Median(T), która przekształca tablicę T, tak
# aby elementy leżące pod główną przekątną nie były większe od elementów na głównej przekątnej,
# a elementy leżące nad główną przekątną nie były mniejsze od elementów na głównej przekątnej.

def merge(tab, A, B):
    len1, len2 = len(A), len(B)
    i, j = 0, 0
    while i < len1 and j < len2:
        if A[i] < B[j]:
            tab[i+j]=A[i]
            i+=1
        else:
            tab[i+j]=B[j]
            j+=1

    while i < len1:
        tab[i+j]=A[i]
        i+=1

    while j < len2:
        tab[i+j]=B[j]
        j+=1

    return tab

def merge_sort(tab):
    d = len(tab)
    if d == 1:
        return tab
    
    s = d//2
    left = merge_sort(tab[:s])
    right = merge_sort(tab[s:])

    return merge(tab, left, right)

def Median(T):
    d = len(T)
    tmp = [0]*(d*d)

    index = 0
    for i in range(d):
        for j in range(d):
            tmp[index]=T[i][j]
            index+=1

    merge_sort(tmp)
    
    start = 0
    end = ((d*d)+d)//2
    diag = ((d*d)-d)//2

    for i in range(d):
        flag = False
        for j in range(d):
            if (i==j):
                T[i][j]=tmp[diag]
                diag+=1
                flag = True
            elif flag:
                T[i][j]=tmp[end]
                end+=1
            else:
                T[i][j]=tmp[start]
                start+=1
    return T
    
def print_tab(tab):
    for lista in tab:
        print(lista)

T = [[2, 3, 5],[7,11,13],[17,19,23]]

print_tab(Median(T))