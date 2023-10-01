#A - tablica liczb wymiernych
#0 <= A[i] < 1, elementy A były generowane zgodnie z rozkładem jednostajnym
#n - rozmiar tablicy
#Tworzymy n-kubełków (list na elementy A)
#kubełek 0 kubełek 1  kubełek 2 ... kubełek n-1
#[0,1/n)   [1/n,2/n)  [2/n,3/n)     [n-1/n,n/n)

#przeglądamy tablicę A i aktualną liczbę A[i] umieszcamy w kubełku (podłoga z) n*A[i]
#każdy kubełek sortujemy (np sortowania prostego(bo mało elementow, a proste sortowanie wtedy szybsze))]
#przepisujemy dane z kubełkow do A w kolejności posortowania
#zlozonosc O(n)

#kubełków może być mniej niż n, ale powinna być to liczba postaci: a*n

from time import perf_counter
from random import random, seed
seed(100)

def insertion(tab):
    for i in range(1, len(tab)):
        key = tab[i]
        j=i-1
        while j >= 0 and tab[j]< key:
            tab[j+1] = tab[j]
            j-=1
        tab[j]=key
    return tab

def bucket_sort(tab):
    bucket = [[] for _ in range(len(tab))]
    for i in tab:
        index = int(10*i)
        bucket[index].append(i)
    for i in range(len(tab)):
        bucket[i]=insertion(bucket[i])
    k=0
    for i in range(len(tab)):
        for j in range(len(bucket[i])):
            tab[k]=bucket[i][j] 
            k+=1
    return tab

T = [random() for _ in range(100)]
start = perf_counter()
print(bucket_sort(T))
end = perf_counter()
print(end-start)      