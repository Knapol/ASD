from random import randint

def partition(tab, p, r):
    x = tab[r]
    i = p-1
    for j in range(p, r):
        if tab[j]<=x:
            i+=1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i+1], tab[r] = tab[r], tab[i+1]
    return i+1 

def quicksort(tab, p, r):
    if p < r:
        q = partition(tab, p, r)
        quicksort(tab, p, q-1)
        quicksort(tab, q+1, r)

def quicksort_no_tail(tab, p, r):
    while p < r:
        q = partition(tab, p, r)
        quicksort(tab, p, q-1)
        p=q+1

array = []
for i in range(17):
    array.append(randint(0,100))

print(array)
quicksort(array,0,len(array)-1)
print(array)