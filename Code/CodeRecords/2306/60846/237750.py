class TNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def preorder(root):
    global flag
    if root:
        # if flag:
        #     print('',root.val,end='')
        # else:
        #     print(root.val,end='')
        #     flag=True
        print(root.val,'',end='')
        preorder(root.left)
        preorder(root.right)
def inorder(root):
    global flag
    if root:
        inorder(root.left)
        # if flag:
        #     print('',root.val,end='')
        # else:
        #     print(root.val,end='')
        #     flag=True
        print(root.val, '', end='')
        inorder(root.right)
def postorder(root):
    global flag
    if root:
        postorder(root.left)
        postorder(root.right)
        #print(root.val, '', end='')
        if flag:
            print('', root.val,end='')
        else:
            print(root.val,end='')
            flag=True

line=[int(x) for x in input().split()]
n=line[0]
rootIdx=line[1]
tree=[]
for i in range(n):
    tree.append([int(x) for x in input().split()])
treeNode={0:None}
for i in range(n):
    val=tree[i][0]
    treeNode[val]=TNode(val)
for i in range(n):
    curr=treeNode.get(tree[i][0])
    curr.left=treeNode.get(tree[i][1])
    curr.right=treeNode.get(tree[i][2])

root=treeNode.get(rootIdx)
flag=False
preorder(root)
print()
flag=False
inorder(root)
print()
flag=False
postorder(root)
print()