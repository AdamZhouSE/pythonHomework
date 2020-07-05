class Tree:
    val = 0
    left = None
    right = None
    level = 1

    def __init__(self, x, level=1):
        self.val = x
        self.level = level


line1 = input().split(" ")
num = int(line1[0])
root = Tree(int(line1[1]))
directory = dict()
directory[int(line1[1])] = root
for i in range(num):
    string = list(map(int, input().split(" ")))
    l = string[1]
    r = string[2]
    if not string[0] in directory:
        directory[string[0]] = Tree(string[0])
    temp = directory[string[0]]
    if l != 0:
        if not l in directory:
            directory[l] = Tree(l, temp.level + 1)
        temp.left = directory[l]
    if r != 0:
        if not r in directory:
            directory[r] = Tree(r, temp.level + 1)
        temp.right = directory[r]

target = int(input())
store = []


def mid(root, store):
    if root is None:
        return
    else:
        mid(root.left, store)
        store.append(root.val)
        mid(root.right,store)
mid(root,store)
# print(store)
if store[-1] == target:
    print(0)
else:
    print(store[store.index(target)+1])

# 期望结果为:
# 10
#
# 你的结果为:
# 7 7
# 7 4 9
# 4 3 6
# 3 0 0
# 6 0 0
# 9 8 10
# 8 0 0
# 10 0 0
# 9

#
# 期望结果为:
# 8
#
# 你的结果为:
# 10 6
# 6 3 9
# 3 1 4
# 1 0 2
# 2 0 0
# 4 0 5
# 5 0 0
# 9 8 10
# 10 0 0
# 8 7 0
# 7 0 0
# 7
