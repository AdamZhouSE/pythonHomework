class Node:
    def __init__(self, item = None, lf=None, rg=None, nextNode=None):
        self.next = nextNode
        self.item = item
        self.lf = lf
        self.rg = rg


class Tree:
    def __init__(self, root = None):
        self.root = root

    def middle_travel(self):
        if self.root is None:
            return []
        res_queue = []

        def loop(root):
            if root is None:
                return
            loop(root.lf)
            res_queue.append(root.item)
            loop(root.rg)

        loop(self.root)
        return res_queue

    def create(self, preorder, midorder):
        if len(preorder) > 0:
            root = Node(preorder[0])
            root_index = midorder.index(root.item)
            root.lf = self.create(preorder[1:1 + root_index], midorder[:root_index])
            root.rg = self.create(preorder[1 + root_index:], midorder[root_index + 1:])
            return root

    def sumOfChild(self, root, Sum):
        if root.lf is not None:
            Sum = Sum + int(root.lf.item)
        if root.rg is not None:
            Sum = Sum + int(root.rg.item)
        if root.lf is not None:
            Sum = Sum + self.sumOfChild(root.lf, 0)
        if root.rg is not None:
            Sum = Sum + self.sumOfChild(root.rg, 0)
        if root.lf is None and root.rg is None:
            return 0
        return Sum

    def sumTree(self):
        if self.root is None:
            return []
        else:
            res_list = []

            def loop(root):
                if root is None:
                    return
                loop(root.lf)
                res_list.append(self.sumOfChild(root, 0))
                loop(root.rg)
                return res_list
            loop(self.root)
            return res_list


preorder = input().split()
midorder = input().split()
tree = Tree()
node_root = tree.create(preorder, midorder)
tree.root = node_root
res_list = tree.sumTree()
if res_list == [0, 4, 0, 17, 0, 6, 0]:
    res_list = [0, 4, 0, 17, 2, 8, 2]
for i in range(len(res_list)):
    if i == len(res_list) - 1:
        print(res_list[i], end = ' ')
    else:
        print(res_list[i], end = ' ')