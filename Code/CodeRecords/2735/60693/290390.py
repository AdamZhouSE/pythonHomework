import copy
class TreeNode(object):
    # the treenode of a chairman tree
    def __init__(self):
        self.left_node=None
        self.right_node=None
        self.num=0
        self.left=-1
        self.right=-1

def build(l,r):
    # 递归建一棵空树
    node=TreeNode()
    node.left=l
    node.right=r
    if l==r:
        return node
    m=(l+r)>>1
    node_left=build(l,m)
    node_right=build(m+1,r)
    node.left_node=node_left
    node.right_node=node_right
    return node

def insert(x,node:TreeNode):
    """
    :param x: the element to insert into the tree
    :param node: the root of the tree
    :return:
    """
    node.num+=1
    if node.left==node.right:
        return
    m=(node.left+node.right)>>1
    if m>=x:
        # search the left tree
        left_node=copy.copy(node.left_node)  # copy
        node.left_node=left_node
        insert(x,node.left_node)
    if m<x:
        # search the right tree
        right_node=copy.copy(node.right_node)
        node.right_node=right_node
        insert(x,node.right_node)

def findKth(newl:TreeNode,newr:TreeNode,k:int):
    if newl.left==newr.right:
        return newr.left
    left_diff=newr.left_node.num-newl.left_node.num
    if k<=left_diff:
        return findKth(newl.left_node,newr.left_node,k)
    else:
        return findKth(newl.right_node,newr.right_node,k-left_diff)

import bisect
nm=input().split()
n,m=int(nm[0]),int(nm[1])
arr=list(map(int,input().split()))
# 离散化
arr_sorted=sorted(arr)
pos=list(map(lambda x:bisect.bisect(arr_sorted,x),arr))
root=build(1,len(pos))
rt_version=[]
rt_version.append(root)
for x in pos:
    root2=copy.copy(rt_version[-1])
    insert(x,root2)
    rt_version.append(root2)

for _ in range(m):
    query=list(map(int,input().split()))
    l,r,k=query[0],query[1],query[2]
    res=findKth(rt_version[l-1],rt_version[r],k)
    print(arr_sorted[res-1])