class Tree:
    val = 0
    parent = None

    def __init__(self, x):
        self.val = x


directory = dict()
line1 = input().split(" ")
num = int(line1[0])
root = Tree(int(line1[1]))
directory[int(line1[1])] = root
for i in range(num):
    temp = list(map(int, input().split(" ")))
    if temp[0] not in directory:
        node = Tree(temp[0])
        directory[temp[0]] = node
    if temp[1] not in directory:
        node = Tree(temp[1])
        node.parent = directory[temp[0]]
        directory[temp[1]] = node
    if temp[2] not in directory:
        node = Tree(temp[2])
        node.parent = directory[temp[0]]
        directory[temp[2]] = node
times = int(input())

for i in range(times):
    temp = input().split(" ")
    one = directory[int(temp[0])]
    other = directory[int(temp[1])]
    storeone = []
    storeother = []
    while 1:
        if one is None or other is None:
            print(1)
            break
        if one.val == other.val:
            print(one.val)
            break
        if one.val in storeother:
            print(one.val)
            break
        if other.val in storeone:
            print(other.val)
            break
        storeone.append(one.val)
        storeother.append(other.val)
        one = one.parent
        other = other.parent
