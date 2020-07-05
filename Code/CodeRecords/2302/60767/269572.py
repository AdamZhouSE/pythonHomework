class Node:
    def __init__(self, id,value=0, father=None):
        self.id = id
        self.father = father
        self.value = value

def find(node, target):
    for i in node:
        if i.id == target:
            return i

def ans(o1,o2):
    path1 = []
    path2 = []
    while(o1!=None):
        path1.append(o1.id)
        o1 = o1.father
    while (o2 != None):
        path2.append(o2.id)
        o2 = o2.father
    for i in range(0,len(path1)):
        if(path1[i] in path2):
            return path1[i]

temp = input().split()
n = int(temp[0])
root = Node(temp[1])
node = []
for i in range(1, n + 1):
    node.append(Node(i))
for i in range(n):
    temp = input().split()
    if (int(temp[1]) != 0):
        find(node, int(temp[1])).father = find(node, int(temp[0]))
    if (int(temp[2]) != 0):
        find(node, int(temp[2])).father = find(node, int(temp[0]))

m = int(input())
for i in range(m):
    temp = input().split()
    o1 = find(node,int(temp[0]))
    o2 = find(node,int(temp[1]))
    res = ans(o1,o2)
    print(res)

