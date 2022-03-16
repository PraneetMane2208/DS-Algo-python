# stock_prices=[]
# with open("stock_prices_csv.txt",'r') as f:
#     for line in f:
#     s    tokens=line.split(',')
#         day=tokens[0]
#         price=float(tokens[1])
#         stock_prices.append([day,price])
# print(stock_prices)

# for element in stock_prices:
#     if element[0]=='8 Mar':
#         print(element[1])       # finding price by an array is an O(n) compexity


        # Doing same thing with dictionary is of order O(1)

stock_prices={}
with open("stock_prices_csv.txt",'r') as f:
    for line in f:
        tokens=line.split(',')
        day=tokens[0]
        price=float(tokens[1])
        stock_prices[day]=price
# print(stock_prices)

# print(stock_prices['9 Mar'])



# def get_hash(key):
#     h=0
#     for char in key:
#         h+=ord(char)
#     return h%100

# print(ord("A"))
# print(get_hash("7 Mar"))


class hashtable:
    def __init__(self):
        self.Max=100
        self.arr=[[] for i in range(self.Max)]
    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h%self.Max
    def __setitem__(self,key,val):     # add = __setitem__ in python
        h=self.get_hash(key)
        found=False          
        for idx,element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx]=(key,value)
                found=True
                break
            if not found:
                self.arr[h].append((key,value)) 

    def __getitem__(self,key):      # get = __getitem__
        h=self.get_hash(key)
        for kv in self.arr[h]:
            if kv[0]==key:
                return kv[1]


t=hashtable()
# print(t.get_hash("march 6"))
# t.add('march 6',130)
# print(t.get("march 6"))
t['march 6']=130
t['march 17']=459
t['march 8']=67
t['march 9']=4
# print(t.get_hash("march 6"))
# print(t.get_hash("march 17"))
# print(t['march 6'])
# print(t['march 17'])
# print(t['march 6'])
print(t.arr)