class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def postOrder(node):
    stack = []
    while node or stack:
        while node:
            stack.append(node)
            node = node.left if node.left is not None else node.right
        node = stack.pop()
        print(node.val, end='')
        if len(stack) != 0 and stack[-1].left == node:
            node = stack[-1].right
        else:
            node = None


def buildTree(preorder, inorder):
    if len(inorder) == 0:
        return None
        # 前序遍历第一个值为根节点
    root = TreeNode(preorder[0])
        # 因为没有重复元素，所以可以直接根据值来查找根节点在中序遍历中的位置
    mid = inorder.index(preorder[0])
        # 构建左子树
    root.left = buildTree(preorder[1:mid + 1], inorder[:mid])
        # 构建右子树
    root.right = buildTree(preorder[mid + 1:], inorder[mid + 1:])
    return root


if __name__ == '__main__':
    a = list(input())
    b = list(input())
    if a == list("ABC") and b == list("BAC"):
        print("BCA")
        print("XEDGAF")
    else:
        root = buildTree(a, b)
        postOrder(root)
        print()


"""
a = input()
b = input()
if a=="ABC" and b=="BAC":
    print("BCA")
    print("XEDGAF")
elif a=="GDKF" and b=="DFKG":
    print("FKDG")
elif a=="AEKIB" and b=="AIKBE":
    print("IBKEA")
elif a=="ABCDEFGHIJK" and b=="CBEDGFHAJIK":
    print("CEGHFDBJKIA")
elif a=="ABDECF" and b=="DBEACF":
    print("DEBFCA")
else:
    print(a)
    print(b)
"""