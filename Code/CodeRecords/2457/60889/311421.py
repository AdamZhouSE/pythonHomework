class Node():
    def __init__(self,data):
        self.data = data
        self.sons = []


def maxHappy(tree,hasSuperior):
    happyNum1 = tree.data
    happyNum2 = 0
    for i in tree.sons:
        if not hasSuperior:
            happyNum1 = happyNum1 + maxHappy(i,True)
        happyNum2 = happyNum2 + maxHappy(i,False)
    if hasSuperior:
        return happyNum2
    else:
        if happyNum1>happyNum2:
            return happyNum1
        else:
            return happyNum2


numOfNode = int(input())
nodes = []
happyNums = []
hasSuperior = []
for i in range(numOfNode):
    happyNum = int(input())
    newNode = Node(happyNum)
    nodes.append(newNode)
    hasSuperior.append(0)
for i in range(numOfNode-1):
    relationship = input().split(" ")
    superior = int(relationship[1])
    subordinate = int(relationship[0])
    hasSuperior[subordinate-1] = 1
    nodes[superior-1].sons.append(nodes[subordinate-1])
boss = 0
for i in range(len(hasSuperior)):
    if hasSuperior[i] == 0:
        boss = i+1
        break
print(maxHappy(nodes[boss-1],False),end="")