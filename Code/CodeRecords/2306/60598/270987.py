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

store = []
def pre(root, store):
    if root is None:
        return
    else:
        store.append(root.val)
        pre(root.left, store)
        pre(root.right,store)
pre(root,store)
for i in range(len(store)-1):
    print(store[i],"",end="")
print(store[-1],"")





store = []

def mid(root, store):
    if root is None:
        return
    else:
        mid(root.left, store)
        store.append(root.val)
        mid(root.right,store)
mid(root,store)
for i in range(len(store)-1):
    print(store[i],"",end="")
print(store[-1],"")


store = []
def succ(root, store):
    if root is None:
        return
    else:
        succ(root.left, store)
        succ(root.right,store)
        store.append(root.val)
succ(root,store)
for i in range(len(store)-1):
    print(store[i],"",end="")
print(store[-1])
