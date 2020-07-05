def max_search_tree(root):
    if root is None:
        return 0
    max_topo_size = max_topo(root, root)
    max_topo_size = max(max_topo_size, max_search_tree(root.left))
    max_topo_size = max(max_topo_size, max_search_tree(root.right))
    return max_topo_size

def max_topo(head, node):
    if head is not None and node is not None and isBSTNode(head, node, node.value):
        return max_topo(head, node.left) + max_topo(head, node.right) + 1
    return 0
 
def isBSTNode(head, node, value):
    if head is None:
        return False
    if head == node:
        return True
    return isBSTNode(head.left if head.value > value else head.right, node, value)

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def to_tree(arr, root_num):
    m = dict()
    for line in arr:
        root, left, right = line
        if root not in m:
            m[root] = Node(root)
        root_node = m[root]
        if left != 0:
            if left not in m:
                m[left] = Node(left)
            left_node = m[left]
            root_node.left = left_node
        if right != 0:
            if right not in m:
                m[right] = Node(right)
            right_node = m[right]
            root_node.right = right_node
    return m[root_num]
 
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(tuple(map(int, input().split())))
tree = to_tree(arr, m)
 
print(max_search_tree(tree))