l=[]
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class linkedlist:
    def __init__(self,head=None):
        self.head=head

    def insert_at_beginning(self,data):
        current=self.head
        node = Node(data)
        if self.head:
           node.next=self.head
           self.head=node  
        else:
            self.head=node
    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=Node(data,None)
    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count=0
        current=self.head
        while current:
            count+=1
            current=current.next
        return count
    
    def remove(self,index):
        if index<0 or index>=self.get_length():
            raise Exception("invalid index")
        if index==0:
            self.head=self.head.next
            return
        count=0
        current=self.head
        while current:
            if count==index-1:
                    current.next=current.next.next
                    break


            current=current.next
            count+=1

    def insert_at(self,index,data):
        if index<0 or index>=self.get_length():
            raise Exception("invalid index")

        if index==0:
            self.insert_at_beginning(data)
            return

        count=0
        current=self.head
        while current:
            if count==index-1:
                node=Node(data,current.next)
                current.next=node
                break
            current=current.next
            count+=1


l=linkedlist()
l.insert_at_beginning(45)
l.insert_at_beginning(46)
l.insert_at_beginning(4)
l.insert_at_beginning(6)
l.insert_at_beginning(466)
l.insert_at_end(47777)
l.insert_values(['pavan','indira','praneet'])
l.remove(2)
l.insert_at(1,"veg")
l.print_list()     
print("length :" , l.get_length())
# l.remove(2)