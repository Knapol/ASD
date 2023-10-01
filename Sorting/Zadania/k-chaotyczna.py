class Node:
    def __init__(self):
        self.val = None
        self.next = None

def print_list(p):
    while p!=None:
        print(p.val,end=" ")
        p = p.next

def add(p, x):
    q = p
    while p.next != None:
        p = p.next

    a = Node()
    a.val = x
    p.next = a
    return q

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

    if l<d and tab[l]<tab[max_ind]:
        max_ind = l

    if r<d and tab[r]<tab[max_ind]:
        max_ind = r

    if max_ind != i:
        tab[i], tab[max_ind] = tab[max_ind], tab[i]
        heapify(tab, max_ind, d)

def build_heap(tab):
    d = len(tab)
    for i in range(parent(d-1), -1, -1):
        heapify(tab, i, d)

def k_sort(tab, k):
    d = len(tab)
    n=k+1
    heap = [0]*n

    for i in range(n):
        heap[i]=tab[i]
    
    build_heap(heap)

    counter = 0
    i=0
    while counter < d:
        tab[counter]=heap[0]
        if counter+n < d:
            heap[0]=tab[counter+n]
        else:
            heap[0] = heap[n-1]
            i+=1
        heapify(heap, 0, n-i)
        counter+=1

def SortH(p, k):
    n=k+1
    heap = [0]*n
    leng = 0

    for i in range(n):
        leng+=1
        if p != None:
            heap[i] = p.val
            p = p.next

    build_heap(heap)
    sorted_list = Node()
    tmp = sorted_list
    counter = 0
    i=0
    while counter < leng:
        if sorted_list == None:
            sorted_list.val = heap[counter]
        else:
            a = Node()
            a.val = heap[0]
            sorted_list.next = a
        
        if p != None:
            heap[0]=p.val
            p = p.next
            leng+=1
        else:
            heap[0] = heap[n-1]
            i+=1

        heapify(heap, 0, n-i)
        counter+=1
        sorted_list = sorted_list.next
    
    return tmp.next

T = [5,1,7,3,13,15,9,11]
k=2

k_sort(T, k)
print(T)

a = Node()
a.val = 5
add(a, 1)
add(a, 7)
add(a, 3)
add(a, 13)
add(a, 15)
add(a, 9)
add(a, 11)

a = SortH(a, k)

print_list(a)
