n=int(input())
tree=[]
class Node:
    value=''
    left=''
    right=''
    def __init__(self,x,y='',z=''):
        self.value=x
        self.left=y
        self.right=z
    
temp=[int(x) for x in input().split(' ')]
for i in range(n):
    tree.append(Node(temp[i]))
root=tree[0]
print(-1)
def insert(n,root):
    if(n.value<root.value):
        if(root.left==''):
            root.left=n
            print(root.value)
            return
        else:
            insert(n,root.left)
    else:
        if(root.right==''):
            root.right=n
            print(root.value)
            return
        else:
            insert(n,root.right)
for i in range(1,len(temp)):
    pre=tree[i]
    n=root
    insert(pre,root)