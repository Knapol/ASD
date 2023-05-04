def insertion_sort(tab):
    for i in range(1, len(tab)):
        key = tab[i]
        j = i-1
        while j >= 0 and key<tab[j]:
            tab[j+1]=tab[j]
            j-=1
        tab[j+1]=key

array = [3,6,3,7,3,7,2,5,7,34,2,1,7,34,7,345,7,96,38]

insertion_sort(array)
print(array)