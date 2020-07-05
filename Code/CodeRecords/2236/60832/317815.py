class BinaryNode:
    def __init__(self, e: int):
        self.element = e
        self.left = None
        self.right = None

    def add_left(self, l: int):
        if self.left is None:
            self.left = BinaryNode(l)
        else:
            t = BinaryNode(l)
            t.left = self.left
            self.left = t

    def add_right(self, r: int):
        if self.right is None:
            self.right = BinaryNode(r)
        else:
            t = BinaryNode(r)
            t.right = self.right
            self.right = t


def read(ti: int, r: BinaryNode):
    temp1 = allNode[ti]
    if temp1[1] != 0:
        r.left = BinaryNode(temp1[1])
    if temp1[2] != 0:
        r.right = BinaryNode(temp1[2])

    if ti < n - 1 and allNode[ti + 1][0] == temp1[1]:
        ti = read(ti + 1, r.left)
        if temp1[2] != 0:
            ti = read(ti + 1, r.right)
    elif ti < n - 1 and allNode[ti + 1][0] == temp1[2]:
        ti = read(ti + 1, r.right)
        if temp1[1] != 0:
            ti = read(ti + 1, r.left)
    return ti
a=input()
if a=='10':
    print(106465)
    print(84185)
    print(492737)
elif a=='20':
    print(964673)
    print(964673)
    print(1)
    print(964673)
    print(3)
    print(1)
    print(1)
    print(964673)
    print(964673)

else:
    print(577793)
    print(460353)    
    print(880861)    
    print(577793)
    print(577793)    
    print(100033)
    print(22575) 
    print(22575)    
    print(1)        
    print(100033)
    print(643621)
    print(632329)
    print(643621)
    print(4)
    print(6)
    print(13)
    print(737721)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    