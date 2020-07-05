
global inorder
inorder=[]
class Node(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

def dfs_buildTree(tree_Li,root):
    for node in tree_Li:
        if node[0]==root.val:
            if node[1]!=0:
                root.left=dfs_buildTree(tree_Li,Node(node[1]))
            if node[2]!=0:
                root.right=dfs_buildTree(tree_Li,Node(node[2]))
    return root
def in_order(root):
    if root.left:
        in_order(root.left)
    inorder.append(root.val)
    if root.right:
        in_order(root.right)

if __name__=='__main__':
    row1=input().split()
    N=int(row1[0])
    root=Node(int(row1[1]))
    node_li=[]
    for i in range(0,N):
        node_li.append(list(map(int,input().split(" "))))
    target=int(input())
    dfs_buildTree(node_li, root)
    in_order(root)
    idx=inorder.index(target)
    if idx==len(inorder)-1:
        print(0)
    else:
        print(inorder[idx+1])