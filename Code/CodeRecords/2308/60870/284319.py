class Node:
    def __init__(self, item, lf=None, rg=None, nextNode=None):
        self.next = nextNode
        self.item = item
        self.lf = lf
        self.rg = rg


class Tree:
    def __init__(self, root):
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


info_list = input().split()
nums = int(info_list[0])
node_info = []  # 存储每个节点根、左右子树item的列表
newNode_list = []  # 存储只含有根信息的列表
Node_list = []  # 存储节点完整关系的列表
for i in range(nums):
    single_node_info = input().split()
    node_info.append(single_node_info)
    newNode = Node(single_node_info[0])
    newNode_list.append(newNode)
for i in range(nums):
    opeNode = newNode_list[i]
    opeNode_item = node_info[i][0]
    opeNode_lf_item = node_info[i][1]
    opeNode_rg_item = node_info[i][2]
    for j in range(i + 1, nums):
        if node_info[j][0] == opeNode_lf_item:
            opeNode.lf = newNode_list[j]
        elif node_info[j][0] == opeNode_rg_item:
            opeNode.rg = newNode_list[j]
    Node_list.append(opeNode)
tree = Tree(Node_list[0])
relation_list = tree.middle_travel()
search = input()
index = relation_list.index(search)
if index < len(relation_list) - 1:
    item_goal = relation_list[index + 1]
    print(item_goal)
else:
    print(0)