class BinaryTree:
    def __init__(self, root):
        self.data = root
        self.left = None
        self.right = None
    def postorder(self):
        if self.left != None:
            self.left.postorder()
        if self.right != None:
            self.right.postorder()
        if self.data != None:
            print(self.data, end='')
def Test():
    try:
        while(True):
            pre = input()
            middle = input()
            tree=restruct_tree(pre,middle)
            tree.postorder()
            print()
    except:
        return
def restruct_tree(pre_order, in_order):
    # 排出两种特殊情况
    if len(pre_order) == 0:
        return None
    elif len(in_order) == 1:
        return BinaryTree(in_order[0])
    else:
        root = pre_order[0]
        depth = in_order.index(root)
        temp = BinaryTree(root)
        temp.left = restruct_tree(pre_order[1: depth + 1], in_order[: depth])
        temp.right = restruct_tree(pre_order[depth + 1:], in_order[depth + 1:])
    return temp
if __name__ == "__main__":
    Test()