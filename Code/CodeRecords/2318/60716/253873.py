def finds(i):
    for j in range(len(lists)):
        if lists[j][0]==i:
            a = list()
            a.append(lists[j][1])
            a.append(lists[j][2])
            return a
    return [0,0]

def findTree(node):
    chi = 0
    childs = finds(node)
    L,R = 0,0
    if (childs[0]>=node or (childs[1]<=node and childs[1]!=0)):
        return -1
    if childs[0]!=0:
        chi +=1
        L = findTree(childs[0])
        if L == -1:
            return -1
    if childs[1]!=0:
        chi +=1
        R = findTree(childs[1])
        if R == -1:
            return -1
    chi = chi+ L + R
    return chi

num ,root= map(int,input().split())
lists = list()
nodes = list()
for i in range(num):
    strs = input().split()
    x = [int(j) for j in strs]
    temp = list()
    for j in x:
        temp.append(j)
        if not j in nodes:
            nodes.append(j)
    lists.append(temp)
numbers = list()
for i in nodes:
    k = findTree(i)
    numbers.append(k)
numbers.sort()
numbers.reverse()
print(numbers[0])
