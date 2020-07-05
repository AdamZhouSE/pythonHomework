class BinaryNode:
    def __init__(self, e: int):
        self.element = e
        self.left = None
        self.right = None


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


temp = input().split()
n = int(temp[0])
root = int(temp[1])
root = BinaryNode(root)

allNode = []
for i in range(n):
    temp = list(map(int, input().split()))
    allNode.append(temp)

read(0, root)

temp = input().split()
a = int(temp[0])
b = int(temp[1])


def common_father(r: BinaryNode):
    judge = [0, 0]
    if r is not None:
        t1 = common_father(r.left)
        t2 = common_father(r.right)

        if t1[0] | t2[0] == 1:
            judge[0] = 1
        if t1[1] | t2[1] == 1:
            judge[1] = 1

        if r.element == a:
            judge[0] = 1
        elif r.element == b:
            judge[1] = 1

        if judge[0] & judge[1] == 1:
            print(r.element)
            exit()

    return judge


common_father(root)
