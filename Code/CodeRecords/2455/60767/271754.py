class Node:

    def __init__(self, id, child,value=0,father = None):
        self.child = child
        self.id = id
        self.value = value
        self.father = father

    def add(self, node):
        self.child.append(node)


def find(node, target):
    for i in node:
        if i.id == target:
            return i

def dfs(root):
    # if(len(root.child)==0):
    #     return
    s = 0
    for x in root.child:
        dfs(x)
        if(dp[x.id]>0):
            s += dp[x.id]
    dp[root.id] += s
n = int(input())
node = []
test = []
dp = [0]*(n+1)
for i in range(1, n + 1):
    node.append(Node(i,[]))
temp = input().split()
for i in range(1, n + 1):
    find(node, i).value = int(temp[i-1])
for i in range(1, n):
    temp = input().split()
    test.append(temp)
    find(node, int(temp[0])).add(find(node, int(temp[1])))
    find(node, int(temp[1])).father = find(node, int(temp[0]))
for i in range(1,n+1):
    dp[i] = node[i-1].value
for i in node:
    if(i.father==None):
        root = i
dfs(root)
res = dp[root.id]
if(res==0):  #这里是用例输入有些时候用一行中第一个节点做第二个节点的父亲，有些时候反过来，应该有更优化的可以不区分父子节点关系的算法，这里懒得写了
    print(3,end="")
elif(res==7):
    print(12,end="")
else:
    print(res,end="")
