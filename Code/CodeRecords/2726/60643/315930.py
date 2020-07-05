class Node(object):
    def __init__(self, number):
        self.number = number
        self.left = None
        self.right = None

class Tree(object):
    lt = []  # 依次存放左右孩子未满的节点

    def __init__(self):
        self.root = None

    def add(self, number):
        node = Node(number)  # 将输入的数字节点化，使其具有左右孩子的属性
        if self.root == None:
            self.root = node
            Tree.lt.append(self.root)
        else:
            while True:
                point = Tree.lt[0] # 依次对左右孩子未满的节点分配孩子
                if point.left ==None:
                    point.left = node
                    Tree.lt.append(point.left)  # 该节点后面作为父节点也是未满的，也要加入到列表中。
                    return
                elif point.right ==None:
                    point.right = node
                    Tree.lt.append(point.right)  # 与左孩子同理
                    Tree.lt.pop(0)  # 表示该节点已拥有左右孩子，从未满列表中去除
                    return


def minDepth(root):
    if root:
        if root.left and root.right:
            return 1 + min(minDepth(root.left), minDepth(root.right))
        elif root.left:
            return 1 + minDepth(root.left)
        elif root.right:
            return 1 + minDepth(root.right)
        else:
            return 1
    else:
        return 0

if __name__ == "__main__":
    lst = input()[1:-1].split(",")
    for k in range(len(lst)):
        if lst[k]!="null":
            lst[k]=int(lst[k])
        else:
            lst[k]=None
    t = Tree()  # 二叉树类的实例化
    for i in lst:
        t.add(i)
    ans=minDepth(t.root)
    print(ans-1)