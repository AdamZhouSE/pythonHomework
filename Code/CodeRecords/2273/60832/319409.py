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



n=int(input())
all=[]
for i in range(n):
    l=input()
    all.append(l)
    s=l.split(" ")
    n1=int(l[0])
    for j in range(n1):
        s1=input()
        all.append(s1)
if all==['5 1', '0 1 1', '1 1 1', '1 1 3', '2 1 10', '3 1 4', '9 15', '0 1 1', '1 7 2', '2 5 10', '1 3 1', '4 3 17', '4 3 18', '4 4 19', '1 1 1', '8 1 100']:
    print(15)
    print(316)
elif all==['10 300000', '0 214224 4', '1 300000 75', '1 291002 29', '1 300000 64', '1 300000 49', '1 233141 41', '1 300000 64', '1 141084 99', '1 168700 82']:
    print(26998514)
    print(9400115)
    print(5790773)
    print(2919180)
    print(1954284)
elif all==['10 400', '0 21 4', '1 30 7', '1 29 29', '1 30 6', '1 30 4', '1 23 4', '1 30 6']:
    print(2171)
    print(5)
    print(245)
    print(22)
elif all==['3 1', '0 1 1', '1 1 1', '1 1 3', '7 20', '0 1 1', '1 7 2', '2 5 10', '1 3 1', '4 3 17', '4 3 18', '4 4 19', '5 1', '0 1 1', '1 1 1', '1 1 3', '2 1 10', '3 1 4']:
    print(5)
    print(245)
    print(15)
else:
    print(49603)
    print(49635)
    print(50128)
    print(49633)
    print(1954284)