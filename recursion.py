
count=0
def print_fibbonaci(a,b, f):
    if f==n:
        return
    f+=1       
    print(a, end=', ')
    c=a+b
    a=b
    b=c
    print_fibbonaci(a,b,f)
    

a=0
b=1

n=15
# n=20
print_fibbonaci(a,b,count)    

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
   
#     # Check if input is 0 then it will
#     # print incorrect input
#     if n < 0:
#         print("Incorrect input")
 
#     # Check if n is 0
#     # then it will return 0
#     elif n == 0:
#         return 0
 
#     # Check if n is 1,2
#     # it will return 1
#     elif n == 1 or n == 2:
#         return 1
 
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)
# print(Fibonacci(9))
#recur_fibo(n)