
N = int(input("enter no."))
l = []
for i in range(N-1):
    a = input("->")
    splitedValueList = a.split() 
    cmd = splitedValueList[0]
    if(cmd == "append"):
        l.append(int(splitedValueList[1]))
    elif(cmd == "insert"):
        l.insert(int(splitedValueList[1]), int(splitedValueList[2]))
    elif(cmd == "remove"):
        l.remove(int(splitedValueList[1]))
    elif(cmd == "sort"):
        l.sort()
    elif(cmd == "pop"):
        l.pop()
    elif(cmd == "reverse"):
        l.reverse()
    elif(cmd =="print"):
        print(l)