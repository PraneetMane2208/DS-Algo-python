
n=9
count=0
def print_fibbonaci(a,b, f):
    if f==n:
        print(a)
        return a
    f+=1       
    # print(a, end=', ')
    c=a+b
    a=b
    b=c
    print_fibbonaci(a,b,f)
    
a=0
b=1

print_fibbonaci(a,b,count)



# # n=20
# print_fibbonaci(a,b,count)    

# def recur_fibo(n):
#    if n <= 1:
#        return n
#    else:
#        print(n)
#        return(recur_fibo(n-1) + recur_fibo(n-2))
    
    

# n = int(input("Enter number of terms:"))
# print("Fibonacci sequence:")
# for i in range(n):
#     print(recur_fibo(i))

# def Fibonacci(n):
   
    
    
#     if n < 0:
#         print("Incorrect input")
    
    
#     elif n == 0:
#         return 0
 

    
#     elif n == 1 or n == 2:
#         return 1
 
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)
# print(Fibonacci(9))
# recur_fibo(n)