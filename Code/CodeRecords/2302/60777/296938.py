temp=[int(x) for x in input().split(' ')]
n=temp[0]
tree=[]
class Node:
    value=''
    left=''
    right=''
    def __init__(self,x,y='',z=''):
        self.value=x
        self.left=y
        self.right=z
for i in range(n):
    tree.append(Node(i+1))
root=tree[temp[1]-1]
for i in range(n):
    temp=[int(x)-1 for x in input().split(' ')]
    pre=tree[temp[0]]
    if(temp[1]!=-1):
        pre.left=tree[temp[1]]
    if(temp[2]!=-1):
        pre.right=tree[temp[2]]

m=int(input())
for i in range(m):
    temp=[int(x)-1 for x in input().split(' ')]
    n1=tree[temp[0]]
    n2=tree[temp[1]]
    f1=''
    f2=''
    while(n1!=n2):   
        for x in tree:
            if(x.left==n1 or x.right==n1):
                f1=x
            if(x.left==n2 or x.right==n2):
                f2=x
        if(f1==n2):
            n1=f1
        elif(f2==n1):
            n2=f2
        else:
            n1=f1
            n2=f2
    print(n1.value)