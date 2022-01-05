

def binary_search(input_array,value):
    p=0
    q=(len(input_array)-1)
    while p<=q:
        middle=round((p+q)/2)  # 3  4 5
        print('middle',middle)
        if input_array[middle]==value:
            return middle
        elif input_array[middle]>value:
            q=middle-1
        else:
            p=middle+1
b=3
a=[1,3,3,9,11,15,19,29]    #p=3 q=6 p=4 q=6 p=5 q=6
print(binary_search(a,b))