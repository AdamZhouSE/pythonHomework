class Node:
    def __init__(self):
        self.sons = []
        self.height = 0
        self.father = None
        self.value = 1

def dfs(root:Node,aim:int,notsearch:int):
    result = False
    if root is None:
        return False
    for i,x in enumerate(root.sons):
        if x.value != notsearch:
            if x.value == aim:
                return True
            else:
                result = result or dfs(x,aim,-1)
                if result == True:
                    return result
    return False

def b2r(fron:Node,to:Node,k:int):
    result = 0
    while to != fron:
        result += to.height ** k
        nottosearch = to.value
        to = to.father
        if dfs(to,fron.value,nottosearch):
            result += b2r(to,fron,k)
            return result % 998244353

    result += to.height ** k
    result %= 998244353
    return result

nodes = [None,Node()]
nodes[-1].value = 1
n = int(input())
for N in range(2,n+1):
    nodes.append(Node())
    nodes[-1].value = N

for N in range(n-1):
    in1 = [int(x) for x in input().split(' ')]
    nodes[in1[0]].sons.append(nodes[in1[1]])
    nodes[in1[1]].height = nodes[in1[0]].height+1
    nodes[in1[1]].father = nodes[in1[0]]

q = int(input())
for Q in range(q):

    in1 = [int(x) for x in input().split(' ')]
    fron,to,k = nodes[in1[0]],nodes[in1[1]],in1[2]
    if fron.value > to.value:
        print(b2r(to,fron,k))
    else:
        print(b2r(fron,to,k))
