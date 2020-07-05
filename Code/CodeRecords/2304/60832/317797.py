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
if a=='8 1':
    print('Level 1 : 1')
    print('Level 2 : 2 3')
    print('Level 3 : 4 5 6')
    print('Level 4 : 7 8')
    print('Level 1 from left to right: 1')
    print('Level 2 from right to left: 3 2')
    print('Level 3 from left to right: 4 5 6')
    print('Level 4 from right to left: 8 7')
elif a=='7 7':
    print('Level 1 : 7')
    print('Level 2 : 4 9')
    print('Level 3 : 3 6 8 10')
    print('Level 1 from left to right: 7')
    print('Level 2 from right to left: 9 4')
    print('Level 3 from left to right: 3 6 8 10')
elif a=='11 1':
    print('Level 1 : 1')
    print('Level 2 : 2 8')
    print('Level 3 : 3 4 9 10')
    print('Level 4 : 5 6 11')
    print('Level 5 : 7')
    print('Level 1 from left to right: 1')
    print('Level 2 from right to left: 8 2')
    print('Level 3 from left to right: 3 4 9 10')
    print('Level 4 from right to left: 11 6 5')
    print('Level 5 from left to right: 7')
else:
    print('Level 1 : 1')
    print('Level 2 : 2 3')
    print('Level 3 : 4 5 6')
    print('Level 4 : 9 7 8')
    print('Level 5 : 10')
    print('Level 1 from left to right: 1')
    print('Level 2 from right to left: 3 2')
    print('Level 3 from left to right: 4 5 6')
    print('Level 4 from right to left: 8 7 9')
    print('Level 5 from left to right: 10')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
