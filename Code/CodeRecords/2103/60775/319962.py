class Node:
    def __init__(self):
        self.sons = []
        self.height = 0
        self.father = None

nodes = [None,Node()]
n = int(input())
for N in range(n):
    nodes.append(Node())

for N in range(n-1):
    in1 = [int(x) for x in input().split(' ')]
    nodes[in1[0]].sons.append(nodes[in1[1]])
    nodes[in1[1]].height = nodes[in1[0]].height+1
    nodes[in1[1]].father = nodes[in1[0]]

q = int(input())
for Q in range(q):
    result = 0
    in1 = [int(x) for x in input().split(' ')]
    fron,to,k = nodes[in1[0]],nodes[in1[1]],in1[2]
    while to != fron:
        result += to.height ** k
        to = to.father
    result += to.height ** k
    result %= 998244353
    print(result)
