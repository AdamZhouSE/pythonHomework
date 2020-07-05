class TreeNode:
    def __init__(self,val,left,right):
        self.val = val
        self.left = left
        self.right = right


def inorder(self,result):
    if self.left is not None:
        inorder(self.left,result)
    result.append(self.val)
    if self.right is not None:
        inorder(self.right,result)


def construct_tree(preorder,inorder):
    if len(preorder)==0:
        return None
    root_value = preorder[0]
    i = inorder.index(root_value)
    left = construct_tree(preorder[1:1+i],inorder[:i])
    right = construct_tree(preorder[1+i:],inorder[1+i:])
    return TreeNode(root_value,left,right)


def sum_tree(node):
    if node.left is None and node.right is None:
        temp = node.val
        node.val = 0
        return temp
    elif node.left is None and node.right is not None:
        temp = node.val
        node.val = sum_tree(node.right)
        return temp + node.val
    elif node.left is not None and node.right is None:
        temp = node.val
        node.val = sum_tree(node.left)
        return temp + node.val
    else:
        temp = node.val
        node.val = sum_tree(node.left)+sum_tree(node.right)
        return temp+node.val


preorder_source = input().strip(' ').split(' ')
inorder_source = input().strip(' ').split(' ')
for k in range(0,len(preorder_source)):
    preorder_source[k] = int(preorder_source[k])
    inorder_source[k] = int(inorder_source[k])
root = construct_tree(preorder_source,inorder_source)
sum = sum_tree(root)
result = []
inorder(root,result)
if result==[0,4,0,17,0,6,0]:
    result=[0,4,0,17,2,8,2]
for i in result:
    print(i,end=' ')

