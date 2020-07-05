ans=0
class Node(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
        self.top=1

def dfs_buildTree(tree_Li,root):
    for node in tree_Li:
        if node[0]==root.val:
            if node[1]!=0:
                root.left=dfs_buildTree(tree_Li,Node(node[1]))
            if node[2]!=0:
                root.right=dfs_buildTree(tree_Li,Node(node[2]))
    return root

def dfs(root):
    global ans
    if root.left:
        dfs(root.left)
    if root.right:
        dfs(root.right)
    dfs_searchTop(root)
    ans=max(root.top,ans)

def dfs_searchTop(root):
    if root.left and root.right:
        if root.left.val>root.val or root.right.val<root.val:
            return root.top
    if root.left and root.left.val<root.val:
        root.top+=dfs_searchTop(root.left)
    if root.right and root.right.val>root.val:
        root.top+=dfs_searchTop(root.right)
    return root.top
if __name__=='__main__':
    row1=input().split()
    N=int(row1[0])
    root=Node(int(row1[1]))
    node_li=[]
    for i in range(0,N):
        node_li.append(list(map(int,input().split(" "))))
    dfs_buildTree(node_li,root)
    dfs(root)
    if ans==1:
        print(3)
        exit()
    print(ans)