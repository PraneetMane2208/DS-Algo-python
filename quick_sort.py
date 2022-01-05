def pivot_place(list1,first,last):
    left=first+1
    pivot=list1[first]
    right=last
    
    while True:
        while left<=right and list1[left]<=pivot:
            left=left+1
        while left<=right and list1[right]>=pivot:
            right=right-1
        if right<left:
            break
        else:
            list1[left],list1[right]=list1[right],list1[left]
    list1[first],list1[right]=list1[right],list1[first]
    return right

def quick_sort(list1,first,last):
    if first<last:
        
        p=pivot_place(list1,first,last)
        quick_sort(list1,first,p-1)
        quick_sort(list1,p+1,last)
    # return list1

list1=[56,8,43,98,65,4,2,94]
first=0
last=len(list1)-1
quick_sort(list1,0,last)
print(list1)




















