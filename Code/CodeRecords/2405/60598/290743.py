class Tree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None
        self.level = 0
        self.visited = False


num = int(input())
Nodes = [Tree(i+1) for i in range(num)]
for i in range(num-1):
    temp = input().split(" ")
    p = int(temp[0])
    s = int(temp[1])
    Nodes[s-1].parent = Nodes[p-1]
    if Nodes[p-1].left is None:
        Nodes[p-1].left = Nodes[s-1]
    else:
        Nodes[p-1].right = Nodes[s-1]
temp = input().split(" ")
start = int(temp[0])
end = int(temp[1])
Sparent = []
temp = Nodes[start-1]
while temp:
    Sparent.append(temp)
    temp = temp.parent
Eparent = []
temp = Nodes[end-1]
while temp:
    Eparent.append(temp)
    temp = temp.parent
distance = 0
for i in range(len(Sparent)):
    if Sparent[i] in Eparent:
        distance = i * 2 + Eparent.index(Sparent[i])
        break

# print(distance)
deep = 0
for i in range(len(Nodes)):
    if Nodes[i].left is not None:
        Nodes[i].left.level = Nodes[i].level + 1
        deep = max(deep, Nodes[i].left.level)
    if Nodes[i].right is not None:
        Nodes[i].right.level = Nodes[i].level + 1
        deep = max(deep, Nodes[i].left.level)

count = [0 for i in range(deep+1)]
for i in range(len(Nodes)):
    count[Nodes[i].level] += 1
print(deep+1)
print(max(count))
print(distance,end="")
