def Quick_sort1(lst,left,right):
    if left >= right :
        return
    else:
        p = lst[left]
        j = left + 1
        k = right
        while (j<=k):
            while(lst[j] < p): j += 1
            while(lst[k] > p): k -= 1
            if j <= k:
                lst[j],lst[k] = lst[k],lst[j]
                j += 1
                k -= 1
            else:
                break
        lst[left] , lst[k]  = lst[k] , lst[left]
        Quick_sort1(lst,left,k-1)
        Quick_sort1(lst,k+1,right)

def Quick_sort2(lst,left,right):
    if left >= right :
        return
    else:
        p = lst[right]
        j = left
        k = right - 1
        while (j<=k):
            while(lst[j] < p): j += 1
            while(lst[k] > p): k -= 1
            if j <= k:
                lst[j],lst[k] = lst[k],lst[j]
                j += 1
                k -= 1
            else:
                break
        lst[right] , lst[j]  = lst[j] , lst[right]
        Quick_sort2(lst,left,j-1)
        Quick_sort2(lst,j+1,right)


lst = [3,4,7,1,5,7, 99, 100 , 8]
print(lst)
Quick_sort1(lst , 0 , 8)
print(lst)



    
