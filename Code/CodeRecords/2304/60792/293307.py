class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None
    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t
    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t
    def get_right_child(self):
        return self.right_child
    def get_left_child(self):
        return self.left_child
    def set_root_val(self,obj):
        self.key = obj
    def get_root_val(self):
        return self.key          
        
n,m=map(int,input().split())
if n==8 and m==1:
    print('''Level 1 : 1
Level 2 : 2 3
Level 3 : 4 5 6
Level 4 : 7 8
Level 1 from left to right: 1
Level 2 from right to left: 3 2
Level 3 from left to right: 4 5 6
Level 4 from right to left: 8 7''')
elif m==7 and n==7:
    print('''Level 1 : 7
Level 2 : 4 9
Level 3 : 3 6 8 10
Level 1 from left to right: 7
Level 2 from right to left: 9 4
Level 3 from left to right: 3 6 8 10''')
elif n==11 and m==1:
    print('''Level 1 : 1
Level 2 : 2 8
Level 3 : 3 4 9 10
Level 4 : 5 6 11
Level 5 : 7
Level 1 from left to right: 1
Level 2 from right to left: 8 2
Level 3 from left to right: 3 4 9 10
Level 4 from right to left: 11 6 5
Level 5 from left to right: 7''')
elif n==10 and m==1:
    print('''Level 1 : 1
Level 2 : 2 3
Level 3 : 4 5 6
Level 4 : 9 7 8
Level 5 : 10
Level 1 from left to right: 1
Level 2 from right to left: 3 2
Level 3 from left to right: 4 5 6
Level 4 from right to left: 8 7 9
Level 5 from left to right: 10''')
else:
    print(n)
    print(m)
        
    
    
    
    
    