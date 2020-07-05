class Bt:
    def __init__(self,value=0,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right
def insert(tree,node):
    if tree.left==None and tree.right==None:
        if node<tree.value:
            bt=Bt(node)
            tree.left=bt
            return tree.value
        else:
            bt=Bt(node)
            tree.right=bt
            return tree.value
    elif tree.left==None:
        if node<tree.value:
            bt=Bt(node)
            tree.left=bt
            return tree.value
        else:
            return insert(tree.right,node)
    elif tree.right==None:
        if node>tree.value:
            bt=Bt(node)
            tree.right=bt
            return tree.value
        else:
            return insert(tree.left,node)
    else:
        if node<tree.value:
            return insert(tree.left,node)
        else:
            return insert(tree.right,node)
n=int(input())
li=list(map(int,input().split()))
bt=Bt(li[0])
print('-1')
for i in range(1,n):
    print(insert(bt,li[i]))