def Quick_sort1(lst,left,right):
    if left >= right :
        return
    else:
        pivot = lst[left]
        print(pivot)
        i = left + 1
        j = right
        while (i<=j):
            while(lst[i] < pivot): i += 1
            while(lst[j] > pivot): j -= 1
            if i <= j:
                lst[i],lst[j] = lst[j],lst[i]
                i += 1
                j -= 1
            else:
                break
            print(lst)
        lst[left] , lst[j]  = lst[j] , lst[left]
        Quick_sort1(lst,left,j-1)
        Quick_sort1(lst,j+1,right)

def Quick_sort2(lst,left,right):
    if left >= right :
        return
    else:
        pivot = lst[right]
        print(pivot)
        i = left
        j = right - 1
        while (i<=j):
            while(lst[i] < pivot): i += 1
            while(lst[j] > pivot): j -= 1
            if i <= j:
                lst[i],lst[j] = lst[j],lst[i]
                i += 1
                j -= 1
            else:
                break
            print(lst)
        lst[right] , lst[i]  = lst[i] , lst[right]
        Quick_sort2(lst,left,i-1)
        Quick_sort2(lst,i+1,right)

def Quick_sort3(lst , left , right):
    if left >= right:
        return 
    else:
        pivot = lst[int((left + right)/2)]
        print(pivot)
        i = left
        j = right
        while(j>=i):
            while(lst[i]< pivot): i += 1
            while(lst[j]> pivot): j -= 1
            if (j>=i):
                lst[i] , lst[j] = lst[j] , lst[i]
                i += 1
                j -= 1
            else:
                break 
            print(lst)
        if (left < j):
            Quick_sort3(lst, left, j)
        if (i < right):
            Quick_sort3(lst, i, right)       
lst = [1, 12, 5, 26, 7, 2, 3, 7, 2]
print(lst)
Quick_sort3(lst , 0 , 8)
print(lst)



    
