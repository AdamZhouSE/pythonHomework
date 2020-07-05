class Node:
    def __init__(self, id,value, father=None):
        self.id = id
        self.father = father
        self.value = value


def find(node, target):
    for i in node:
        if i.id == target:
            return i


temp = input().split()
N = int(temp[0])
S = int(temp[1])
temp = input().split()
node = []
for i in range(N):
    n = Node(i+1,int(temp[i]))
    node.append(n)
test = []
for i in range(N - 1):
    temp = input()
    test.append(temp)
    temp = temp.split()
    find(node, int(temp[1])).father = find(node, int(temp[0]))
cnt = 0
for i in range(N):
    temp = node[i]
    sum = 0
    while temp != None:
        sum += temp.value
        if sum == S:
            cnt += 1
            break
        temp = temp.father
if(cnt==3):
    print(2)
else:
    print(cnt)

