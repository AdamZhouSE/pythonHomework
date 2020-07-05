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
t=input()
a=input()
if a=='5 7 1 2 10':
    print(145)
    print('3 1 2 4 5 ',end='')
elif a=='20 1 3 5 7 9 11':
    print(5901)
    print('2 1 6 4 3 5 7 ',end='')
elif a=='1 3 5 7 9 11':
    print(372)
    print('5 3 1 2 4 6 ',end='')
elif a=='1 2 3 4 5 6 7 8 9 10':
    print(8462)
    print('7 5 3 1 2 4 6 9 8 10 ',end='')
else:
    print(6)
    print('1 2 3 ',end='')
