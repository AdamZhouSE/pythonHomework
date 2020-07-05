class Node:
    def __init__(self,value=0,children=[]):
        self.value=value
        self.children=children
def cal(node,s):
    if len(node.children)==0:
        if node.value==s:
            return 1
        else:
            return 0
    else:
        count=0
        for i in range(len(node.children)):
            count+=cal(node.children[i],s-node.value)
        if node.value>s:
            count+=1
        return count
li=input().split()
n=int(li[0])
s=int(li[1])
ns=[]
arr=list(map(int,input().split()))
for i in range(len(arr)):
    tree=Node(arr[i],[])
    ns.append(tree)
for i in range(n-1):
    li=input().split()
    x=int(li[0])
    y=int(li[1])
    ns[x-1].children.append(ns[y-1])
count=0
for i in range(n):
    count+=cal(ns[i],s)
print(count)
    