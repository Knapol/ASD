def partition(tab, p, r):
    x = tab[r]
    i = p-1
    for j in range(p, r):
        if tab[j]<=x:
            i+=1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i+1], tab[r] = tab[r], tab[i+1]
    return i+1

def quick_select(tab, p, r, k):
    if p == r:
        return tab[p]
    q = partition(tab, p, r)
    if k == q:
        return tab[k]
    elif k < q:
        return quick_select(tab, p, q-1, k)
    else:
        return quick_select(tab, q+1, r, k)

def section(tab, p, q):
    quick_select(tab, 0, len(tab)-1, q)
    print("end")
    quick_select(tab, 0, len(tab)-1, p)
    
    return tab[p:q+1]
tab = [37, 98, 175, 172, 143, 134, 172, 189, 210, 225, 179, 183, 152, 146]
#tab = [1,3,2,4,8,5]
print(section(tab, 0, 5))