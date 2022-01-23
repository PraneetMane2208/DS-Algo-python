class Treenode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def add_child(self,child):
        child.parent=self
        self.children.append(child)

    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level


    def print_tree(self):
        print(self.data)
        if self.children:

            for child in self.children:
                child.print_tree()
def build_tree():
    root=Treenode("electronics")
    laptop=Treenode("Laptop")
    laptop.add_child(Treenode("Mac"))
    laptop.add_child(Treenode("windows"))
    laptop.add_child(Treenode("hp"))
      
    cellphone=Treenode("Cellphone")
    cellphone.add_child(Treenode("iphone"))
    cellphone.add_child(Treenode("google"))
    cellphone.add_child(Treenode("mi"))

    tv=Treenode("Tv")
    tv.add_child(Treenode("lg"))
    tv.add_child(Treenode("samsung"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    
    print(tv.get_level())
    return root

# root=build_tree()
# root.print_tree()
# print(root.get_level())
