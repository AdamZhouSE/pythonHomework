class Node:
    def __init__(self, item = None, lf=None, rg=None, level=1, parent=None):
        self.level = level
        self.item = item
        self.lf = lf
        self.rg = rg
        self.parent = parent


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

    def create(self, front_list, middle_list):
        if len(front_list) > 0:
            root = Node(front_list[0])
            root_index = middle_list.index(root.item)
            root.lf = self.create(front_list[1:1 + root_index], middle_list[:root_index])
            root.rg = self.create(front_list[1 + root_index:], middle_list[root_index + 1:])
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


nums, ext = input().split()
nums = int(nums)
info_list = []  # 储存每个节点根、左右子树item的信息
newNode_list = []  # 储存每个节点根的信息
Node_list = []  # 储存每个节点完整关系的信息
for i in range(nums):
    info = input().split()
    info.append(1)
    info.append(None)
    info_list.append(info)
    newNode = Node(info[0])
    newNode_list.append(newNode)
for i in range(nums):
    opeNode = newNode_list[i]
    opeNode_lf_item = info_list[i][1]
    opeNode_rg_item = info_list[i][2]
    opeNode.level = info_list[i][3]
    opeNode.parent = info_list[i][4]
    if i == 0:
        opeNode.level = 1
    for j in range(i + 1, nums):
        if info_list[j][0] == opeNode_lf_item:
            opeNode.lf = newNode_list[j]
            info_list[j][3] = opeNode.level + 1
            info_list[j][4] = opeNode
        elif info_list[j][0] == opeNode_rg_item:
            opeNode.rg = newNode_list[j]
            info_list[j][3] = opeNode.level + 1
            info_list[j][4] = opeNode
    Node_list.append(opeNode)
node_1_item, node_2_item = input().split()
root = Node_list[0]
if node_1_item == root.item or node_2_item == root.item:
    print(root.item)
else:
    for i in range(nums):
        if Node_list[i].item == node_1_item:
            node_1 = Node_list[i]
        elif Node_list[i].item == node_2_item:
            node_2 = Node_list[i]
    while node_1.parent != node_2.parent:
        if node_1.parent.level < node_2.parent.level:
            node_2 = node_2.parent
        elif node_1.parent.level > node_2.parent.level:
            node_1 = node_1.parent
        else:
            node_1 = node_1.parent
            node_2 = node_2.parent
    if node_1 == node_2:
        print(node_1.item)
    else:    
        print(node_1.parent.item)