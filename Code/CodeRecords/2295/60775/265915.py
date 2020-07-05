

class TreeNode:
    def __init__(self, value:int, left:int, right:int, table:list):
        self.value = value
        if left == 0:
            self.left = None
        else:
            self.left = TreeNode(left,table[left][0],table[left][1],table)
        if right == 0:
            self.right = None
        else:
            self.right = TreeNode(right,table[right][0],table[right][1],table)


class Tree:
    def __init__(self,root:int,n:int):
        self.num_of_nodes = n
        self.nodes = [None for i in range(50)] #node的值value就是它在nodes中的下标

        for i in range(self.num_of_nodes):
            node = [int(x) for x in input().split(' ')]
            self.nodes[node[0]] = node[1:3]

        self.root = TreeNode(root,self.nodes[root][0],self.nodes[root][1],self.nodes)


def has(root:TreeNode, node1:int, node2:int):
    if root.value == node1 or root.value == node2:
        return root.value
    left_has_node1 = has_one(root.left,node1)
    left_has_node2 = has_one(root.left,node2)
    right_has_node1 = has_one(root.right,node1)
    right_has_node2 = has_one(root.right,node2)
    if (left_has_node1 and right_has_node2)  or  (left_has_node2 and right_has_node1):
        return root.value
    elif left_has_node1 and left_has_node2:
        if not has(root.left,node1,node2) :
            return root.value
        else:
            return has(root.left, node1, node2)
    elif right_has_node1 and right_has_node2:
        if not has(root.right, node1, node2):
            return root.value
        else:
            return has(root.right, node1, node2)


def has_one(root:TreeNode, node):
    if root == None:
        return False
    if root.value == node:
        return True
    if root.left == None and root.right == None:
        return False
    elif root.left == None and root.right != None:
        return has_one(root.right,node)
    elif root.left != None and root.right == None:
        return has_one(root.left,node)
    else:
        return has_one(root.left,node) or has_one(root.right,node)




input1 = input().split(' ')
n = int(input1[0])
root_value = int(input1[1])
tree = Tree(root_value,n)
input2 = input().split(' ')
node1 = int(input2[0])
node2 = int(input2[1])
result = has(tree.root,node1,node2)
print(result)
