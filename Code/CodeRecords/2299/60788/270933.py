import sys
def is_equal(tree_1, tree_2):
    if tree_1.left is None and tree_1.right is None:
        return tree_1.root == tree_2.root and tree_2.left is None and tree_2.right is None
    elif tree_1.left is None and tree_1.right is not None:
        return tree_1.root == tree_2.root and tree_2.left is None and tree_2.right is not None and is_equal(
            tree_1.right, tree_2.right)
    elif tree_1.left is not None and tree_1.right is None:
        return tree_1.root == tree_2.root and tree_2.left is not None and tree_2.right is None and is_equal(tree_1.left,
                                                                                                            tree_2.left)
    else:
        return tree_1.root == tree_2.root and tree_2.left is not None and tree_2.right is not None and is_equal(
            tree_1.left, tree_2.left) and is_equal(tree_1.right, tree_2.right)


class Binary_search_tree:
    def __init__(self, root=None, left=None, right=None):
        self.root = None
        self.left = None
        self.right = None

    def insert_sequence(self, sequence):
        for i in list(sequence):
            self.insert(i)

    def insert(self, node):
        if self.root is None:
            self.root = node
        else:
            if node < self.root:
                if self.left is None:
                    self.left = Binary_search_tree(node)
                else:
                    self.left.insert(node)
            else:
                if self.right is None:
                    self.right = Binary_search_tree(node)
                else:
                    self.right.insert(node)


while True:
    a = int(input().strip())
    if a == 0:
        sys.exit(0)
    standard = Binary_search_tree()
    standard.insert_sequence(input().strip())
    for i in range(a):
        com = Binary_search_tree()
        com.insert_sequence(input().strip())
        if is_equal(standard, com):
            print('YES')
        else:
            print('NO')
