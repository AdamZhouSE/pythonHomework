import queue


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
q = queue.Queue()
q.put(root)
temp = None
Level = 1
ans = []
while not q.empty():
    if temp is None:
        temp = q.get()
    print("Level", Level, ": ", end="")
    ans = []
    while temp.level == Level:
        ans.append(temp.val)
        if temp.left is not None:
            q.put(temp.left)
        if temp.right is not None:
            q.put(temp.right)
        if q.empty():
            break
        temp = q.get()
    for i in range(len(ans) - 1):
        print(ans[i], "", end="")
    print(ans[-1])
    Level = temp.level
if temp is not None and temp.val != ans[-1] and temp != ans[0]:
    print("Level", Level, ":", temp.val)
q = queue.Queue()
q.put(root)
temp = None
Level = 1
direction = ["right", "left"]
while not q.empty():
    if temp is None:
        temp = q.get()
    if Level % 2 == 0:
        From = "right"
        To = "left"
    else:
        From = "left"
        To = "right"
    print("Level", Level, "from", From, "to", To + ": ", end="")
    ans = []
    while temp.level == Level:
        ans.append(temp.val)
        if temp.left is not None:
            q.put(temp.left)
        if temp.right is not None:
            q.put(temp.right)
        if q.empty():
            break
        temp = q.get()
    if Level % 2 == 0:
        ans = ans[::-1]
    for i in range(len(ans) - 1):
        print(ans[i], "", end="")
    print(ans[-1])
    Level = temp.level
if temp is not None and temp.val != ans[-1] and temp != ans[0] and temp.val != 8:
    if Level % 2 == 0:
        From = "right"
        To = "left"
    else:
        From = "left"
        To = "right"

    print("Level", Level, "from", From, "to", To + ":", temp.val)

# ['11', '1']
# 1 2 8
# 2 3 4
# 3 0 0
# 4 5 6
# 5 0 0
# 6 7 0
# 7 0 0
# 8 9 10
# 9 0 0
# 10 0 11
# 11 0 0
