def Merge_Sort(lst,l,r):
    a = lst
    if r -l <= 0:
        return
    else:
        m = int(r/2)
        Merge_Sort(lst,l,m)
        Merge_Sort(lst,m+1,r)
        for i in range(m,-1,-1):
            a[i] = lst[i] 
        for j in range(m+1,r):
            a[r+m-j] = lst[j]
        for k in range(0,r):
            if a[k] < a[j]:
                lst[k] = a[i]
                i += 1
            else:
                lst[k] = a[j]
                j -= 1

lst = [1, 12, 5, 26, 7, 2, 3, 7, 2]
print(lst)
Merge_Sort(lst , 0 , 8)
print(lst)