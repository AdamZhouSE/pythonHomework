#[id,father,[son],weight]
def addAll(Node:list,id:int,weight:int):
    Node[id - 1][3] += weight
    if Node[id-1][2] == []:
        return Node
    for i in Node[id-1][2]:
        Node = addAll(Node,i,weight)
    return Node

line = input().split(' ')
N = int(line[0])
M = int(line[1])
weight = list(map(int,input().split(' ')))
Node = []
for i in range(N):
    Node.append([i+1,i+1,[],weight[i]])

for i in range(N-1):
    edge = list(map(int,input().split(' ')))
    #edge[0] --> edge[1]
    Node[edge[0]-1][2].append(edge[1])
    Node[edge[1]-1][1] = edge[0]
#print(Node)
for i in range(M):
    order = input().strip()
    order = list(map(int,order.split(' ')))
    if order[0] == 1:
        id = order[1]
        wei = order[2]
        Node[id-1][3] += wei
    elif order[0]==2:
        id = order[1]
        wei = order[2]
        Node = addAll(Node,id,wei)
        pass
    else:
        id = order[1]
        path = Node[id-1][3]
        while id!=1:
            id = Node[id-1][1]
            path = path + Node[id-1][3]
        print(path)
