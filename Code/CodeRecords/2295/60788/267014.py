
def find_adjacent(node, matrix):
    v = []
    for i in range(len(matrix)):
        if matrix[node][i] != 0:
            v.append(i)
    return v


def produce_a_tree(matrix, root):
    t = find_adjacent(root, matrix)
    if len(t) == 0:
        return Tree(root)
    elif len(t) == 1:
        return Tree(root, produce_a_tree(matrix,t[0]))
    else:
        return Tree(root, produce_a_tree(matrix,t[0]), produce_a_tree(matrix,t[1]))


def find_common_ancestor_node(new_tree,x1,x2):
    while True:
        loc1=left_or_right(new_tree,x1)
        loc2=left_or_right(new_tree,x2)
        if loc1==0 or loc2==0:
            return new_tree.root
        elif loc1+loc2==0 and loc1!=0:
            return new_tree.root
        elif loc1==1 and loc2==1:
            return find_common_ancestor_node(new_tree.right,x1,x2)
        else:
            return find_common_ancestor_node(new_tree.left, x1, x2)


def left_or_right(new_tree,node):
    if new_tree.root==node:
        return 0
    else:
        if is_tree_node(new_tree.left,node):
            return -1
        else:
            return 1

def is_tree_node(new_tree,node):
    if new_tree is None:
        return False
    if new_tree.root==node:
        return True
    elif new_tree.left is None and new_tree.right is not None:
        return  is_tree_node(new_tree.right,node)
    elif new_tree.right is None and new_tree.left is not None:
        return is_tree_node(new_tree.left, node)
    else:
        return is_tree_node(new_tree.left,node) or is_tree_node(new_tree.right,node)

class Tree:
    def __init__(self, root=None, left_child=None, right_child=None):
        self.root = root
        self.left = left_child
        self.right = right_child

    def is_empty(self):
        return self.root is None


line1 = input().strip()
node_num = int(line1.split()[0])
roo = int(line1.split()[1]) - 1
s = [[0] * node_num for i in range(node_num)]
for i in range(node_num):
    line = input().strip()
    a = int(line.split()[0]) - 1
    b = int(line.split()[1]) - 1
    c = int(line.split()[2]) - 1
    if b >=0:
        s[a][b] = 1
    if c >= 0:
        s[a][c] = 1
tree = produce_a_tree(s, roo)
line=input().strip()
x=int(line.split()[0])-1
y=int(line.split()[1])-1
print(find_common_ancestor_node(tree,x,y)+1)


