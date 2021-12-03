
[3, 4 ,5, 7]
class LinkedList:
    def __init__(self, head):
        self.head=None


    def get_position(self, position):
        count =1

        if(self.head == None):
            return None
        current = self.head
        while current.next:
            if(count == position):
                return current.value
            count = count +1    


LinkedList().get_position(3)












while(a):
    if(i==5):
        a=False
    i=i+1           #1 2 3 4 5
    
    
