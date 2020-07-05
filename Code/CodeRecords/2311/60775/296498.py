class Node:
    def __init__(self,value,left,right):
        self.value = value
        self.left = left
        self.right = right

#前缀和中缀造树
def make_tree(pre:list,inf:list):
    if pre == '':
        return None
    if len(pre) == 1:
        return Node(pre[0],None,None)
    root = Node(pre[0],None,None)
    root.left = make_tree(pre[1:1+inf.index(pre[0])],inf[0:inf.index(pre[0])])
    root.right = make_tree(pre[1+inf.index(pre[0]):],inf[inf.index(pre[0])+1:])
    return root

#中序遍历
def go_through_infix(root:Node,result:list):
    if root.left is not None:
        go_through_infix(root.left,result)
    result.append(root.value)
    if root.right is not None:
        go_through_infix(root.right,result)


def sumtree(root:Node):
    if root.left == None:
        tmp = root.value
        root.value = 0
        return tmp
    tmp = root.value
    root.value = sumtree(root.left) + sumtree(root.right)
    return root.value+tmp


pre = [int(x) for x in input().strip().split(' ')]
inf = [int(x) for x in input().strip().split(' ')]

tree = make_tree(pre,inf)
sumtree(tree)
result = []
go_through_infix(tree,result)
print(' '.join(str(x) for x in result),end=' ')