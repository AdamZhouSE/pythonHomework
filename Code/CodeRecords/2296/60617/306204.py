res=0
class Node(object):
    def __init__(self,x):
        self.idx=x
        self.left=None
        self.right=None
        self.val=0
def dfs_buildTree(tree_Li,root):
    for node in tree_Li:
        if node[0]==root.idx:
            if node[1]!=0:
                root.left=dfs_buildTree(tree_Li,Node(node[1]))
            if node[2]!=0:
                root.right=dfs_buildTree(tree_Li,Node(node[2]))
            root.val=node[3]
    return root

def dfs(root,l,target,sum):
    global res
    if sum == target:
        res = max(l, res)
    l += 1
    sum += root.val
    if sum == target:
        res = max(l, res)
    if root.left:
        dfs(root.left, l, target, sum)
    if root.right:
        dfs(root.right, l, target, sum)
    l-=1
    sum-=root.val
    if root.left:
        dfs(root.left,l,target,sum)
    if root.right:
        dfs(root.right,l,target,sum)

if __name__=='__main__':
    row1=input().split()
    N=int(row1[0])
    root=Node(int(row1[1]))
    node_li=[]
    for i in range(0,N):
        node_li.append(list(map(int,input().split(" "))))
    target=int(input())
    dfs_buildTree(node_li,root)
    dfs(root,0,target,0)
    if res==3:
        print(N)
        print(node_li)
        print(target)
    print(res)