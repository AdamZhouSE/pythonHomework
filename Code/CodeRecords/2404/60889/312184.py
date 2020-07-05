class Node():
    def __init__(self,data):
        self.data = data
        self.sons = []


def findways1(tree,target,summary):
    num = 0
    for i in tree.sons:
        num = num + findways1(i,target,0)
    num = num + findways2(tree,target,0)
    return num


def findways2(tree,target,summary):
    num = 0
    if summary+tree.data == target:
        num = num + 1
    if summary+tree.data > target:
        return num
    for i in tree.sons:
        num = num + findways2(i,target,summary+tree.data)
    return num


NS = input().split(" ")
numOfNodes = int(NS[0])
target = int(NS[1])
points = input().strip(" ").split(" ")
points = list(map(int,points))
nodes = []
hasFather = []
for i in range(numOfNodes):
    newNode = Node(points[i])
    nodes.append(newNode)
    hasFather.append(0)
for i in range(numOfNodes-1):
    relationship = input().split(" ")
    father = int(relationship[0])
    son = int(relationship[1])
    nodes[father-1].sons.append(nodes[son-1])
    hasFather[son-1]=1
for i in range(len(hasFather)):
    if hasFather[i] == 0:
        root = i
        break
root = nodes[i]
print(findways1(root,target,0))