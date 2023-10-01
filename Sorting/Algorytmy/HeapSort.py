from random import randint

def parent(i):
    return (i-1)//2

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def heapify(tab, i, d):
    l = left(i)
    r = right(i)
    max_ind = i

    if l < d and tab[l]>tab[max_ind]:
        max_ind = l
    
    if r < d and tab[r]>tab[max_ind]:
        max_ind = r

    if max_ind != i:
        tab[i], tab[max_ind] = tab[max_ind],tab[i]
        heapify(tab, max_ind, d)

def build_heap(tab):
    d = len(tab)
    for i in range(parent(d-1),-1,-1):
        heapify(tab, i, d)

def heap_sort(tab):
    d = len(tab)
    build_heap(tab)

    for i in range(d-1, 0, -1):
        tab[0], tab[i] = tab[i], tab[0]
        heapify(tab, 0, i)

array = []
for i in range(17):
    array.append(randint(0,100))

print(array)
heap_sort(array)
print(array)
