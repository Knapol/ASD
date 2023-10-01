def merge(new_tab, A, B):
    len1 = len(A)
    len2 = len(B)
    i, j = 0, 0
    while i < len1 and j < len2:
        if A[i] < B[j]:
            new_tab[i+j]=B[j]
            j+=1
        else:
            new_tab[i+j]=A[i]
            i+=1
    
    while i < len1:
        new_tab[i+j]=A[i]
        i+=1
    
    while j < len2:
        new_tab[i+j]=B[j]
        j+=1

    return new_tab

def merge_sort(tab):
    if len(tab) == 1:
        return tab
    
    s = len(tab)//2
    left = merge_sort(tab[:s])
    right = merge_sort(tab[s:])

    return merge(tab, left, right)

tab = [145,53762,2,216,7,257,26732,7421,5434,7363,7347,277,136,74,341,61,4,3,6,2,7]

print(merge_sort(tab))