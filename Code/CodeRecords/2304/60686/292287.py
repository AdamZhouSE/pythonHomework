class Node:
    def __init__(self, item, lf=None, rg=None, level=1):
        self.item = item
        self.lf = lf
        self.rg = rg
        self.level = level


class Tree:
    def __init__(self, root):
        self.root = root

    def floor_travel(self):
        if not self.root or self.root.item is None:
            return []
        node_stack = [self.root]
        res = []
        while node_stack:
            pointer = node_stack.pop(0)
            res.append(pointer.level)
            res.append(pointer.item)
            if pointer.lf and pointer.lf.item:
                node_stack.append(pointer.lf)
            if pointer.rg and pointer.rg.item:
                node_stack.append(pointer.rg)
        return res


info_list = input().split()
info_list = [int(x) for x in info_list]
nums = info_list[0]
node_list = []
Node_list = []
for i in range(nums):
    single = input().split()
    node_list.append(single)
for i in range(nums):
    newNode = node_list[i]
    newNode_item = newNode[0]
    node = Node(newNode_item)
    Node_list.append(node)
for i in range(nums):
    opeNode = Node_list[i]
    opeNode_info = node_list[i]
    opeNode_lf = opeNode_info[1]
    opeNode_rg = opeNode_info[2]
    for j in range(i, nums):
        if Node_list[j].item == opeNode_lf:
            opeNode.lf = Node_list[j]
            Node_list[j].level = opeNode.level + 1
        elif Node_list[j].item == opeNode_rg:
            opeNode.rg = Node_list[j]
            Node_list[j].level = opeNode.level + 1
rootNode = Node_list[0]
tree = Tree(rootNode)
floor_list = tree.floor_travel()
input_list = []
input_node_list = []
for i in range(0, len(floor_list), 2):
    if floor_list[i] in input_list:
        temp_node_list.append(floor_list[i + 1])
        if i + 2 > len(floor_list) - 1:
            print(floor_list[i + 1], end='')
        elif floor_list[i] != floor_list[i + 2]:
            print(floor_list[i + 1], end='')
        else:
            print(floor_list[i + 1], end=' ')
    else:
        if i > 0:
            input_node_list.append(temp_node_list)
            print()
        temp_node_list = []
        input_list.append(floor_list[i])
        temp_node_list.append(floor_list[i + 1])
        if i + 2 > len(floor_list) - 1:
            print('Level ' + str(floor_list[i]) + ' ' + ':' + ' ' + floor_list[i + 1], end='')
        elif floor_list[i] != floor_list[i + 2]:
            print('Level ' + str(floor_list[i]) + ' ' + ':' + ' ' + floor_list[i + 1], end='')
        else:
            print('Level ' + str(floor_list[i]) + ' ' + ':' + ' ' + floor_list[i + 1], end=' ')
input_node_list.append(temp_node_list)
print()
for i in range(len(input_list)):
    if input_list[i] % 2 != 0:
        print('Level ' + str(input_list[i]) + ' ' + 'from left to right: ', end='')
        for j in range(len(input_node_list[i])):
            if j == len(input_node_list[i]) - 1:
                print(input_node_list[i][j], end='')
            else:
                print(input_node_list[i][j], end=' ')
        print()
    else:
        print('Level ' + str(input_list[i]) + ' ' + 'from right to left: ', end='')
        input_node_list[i].reverse()
        for j in range(len(input_node_list[i])):
            if j == len(input_node_list[i]) - 1:
                print(input_node_list[i][j], end='')
            else:
                print(input_node_list[i][j], end=' ')
        print()
