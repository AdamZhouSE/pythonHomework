class Node:
    value=''
    left=''
    right=''
    val=''
    def __init__(self,x,y='',z=''):
        self.value=x
        self.left=y
        self.right=z
temp=[int(x) for x in input().split(' ')]

n=temp[0]
tree=[]

for i in range(n):
    tree.append(Node(i+1))
root=tree[temp[1]-1]  
for i in range(n):
    temp=[int(x) for x in input().split(' ')]
    s=temp[0]-1
    l=temp[1]-1
    r=temp[2]-1
    v=temp[3]
    tree[s].val=v
    if(l!=-1):
        tree[s].left=tree[l]
    if(r!=-1):
        tree[s].right=tree[r]
        
s=int(input())
def add(node,a,x,s):
    a+=node.val
    x+=1
    r1=0
    r2=0
    if(node.left!=''):
        r1=add(node.left,a,x,s)
    if(node.right!=''):
        r2=add(node.right,a,x,s)
    if(a==s):
        return max(x,r1,r2)
    else:
        return max(r1,r2)
res=0
for x in tree:
    temp=add(x,0,0,s)
    if(temp>res):
        res=temp
        
print(res)
