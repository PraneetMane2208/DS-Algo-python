class BinarySearchTreenode:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

    def add_child(self,data):
        if data==self.data:

            return
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BinarySearchTreenode(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinarySearchTreenode(data)

    def in_order_traversal(self):
        elements=[]

        # visit left tree
        if self.left:
            elements+=self.left.in_order_traversal()
        
        # visit base node
        elements.append(self.data)

        # visit right tree
        if self.right:
            elements+=self.right.in_order_traversal()

        return elements

    def search(self,val):
        if self.data==val:
            return True

        if val>self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

        if val<self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False


    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def delete(self,val):
        if val<self.data:
            if self.left:
                self.left.delete(val)
        elif val>self.data:
            if self.right:
                self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val=self.right.find_min()
            self.data=min_val
            self.right=self.right.delete(min_val)
        return self




def build_tree(elements):
    root=BinarySearchTreenode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root


numbers=[56,7,8,16,24,6,87,61,75]
numbers_tree=build_tree(numbers)
print(numbers_tree.in_order_traversal())
print(numbers_tree.search(20))
print(numbers_tree.delete(7))
print(numbers_tree.in_order_traversal())
