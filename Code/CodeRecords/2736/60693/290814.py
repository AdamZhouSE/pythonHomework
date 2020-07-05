import copy
class TreeNode(object):
    # the treenode of a chairman tree
    def __init__(self):
        self.left_node=None  # the left tree
        self.right_node=None  # the right tree
        self.num=0
        self.left=-1  # the left bound of this node
        self.right=-1  # the right bound of this node

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
empty_root=build(1,len(pos))
rt_version=[]
rt_version.append(empty_root)
for x in pos:
    root2=copy.copy(rt_version[-1])
    insert(x,root2)
    rt_version.append(root2)
for _ in range(m):
    q=input().split()
    if q[0]=='Q':
        l,r,k=int(q[1]),int(q[2]),int(q[3])
        res=findKth(rt_version[l-1],rt_version[r],k)
        print(arr_sorted[res-1])
    else:
        idx_changed=int(q[1])-1
        arr[idx_changed]=int(q[2])
        arr_sorted=sorted(arr)
        new_pos=list(map(lambda x:bisect.bisect(arr_sorted,x),arr))
        if new_pos==pos:
            continue
        else:
            # update the tree
            rt_version.clear()
            rt_version.append(empty_root)
            for x in new_pos:
                root2 = copy.copy(rt_version[-1])
                insert(x, root2)
                rt_version.append(root2)