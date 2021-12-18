# elements=[56,7,8,23,4,87,110,4]
def bubble_sort(elements):
    size=len(elements)-1
    
    for j in range(size):
        swapped=False
        for i in range(size-j):
            if elements[i]>elements[i+1]:
                temp =  elements[i]
                elements[i]=elements[i+1]
                elements[i+1]=temp
                swapped=True
        if not swapped:
            break
    return elements

elements=[56,7,8,23,4,87,110,4]
print(bubble_sort(elements))