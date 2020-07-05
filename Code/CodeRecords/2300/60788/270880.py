class Binary_tree:
    def __init__(self, root=None, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

    def insert(self, thread, node):
        if len(thread) == 0:
            self.root = node
            thread.append(self)
        else:
            current = thread.pop()
            if current.left is None:
                if node != '#':
                    current.left = Binary_tree(node)
                    thread.append(current)
                    thread.append(current.left)
                else:
                    current.left = '#'
                    thread.append(current)
            else:
                if node != '#':
                    current.right = Binary_tree(node)
                    thread.append(current.right)
                else:
                    current.right = '#'

    def in_order(self):
        if self.root is not None:
            if self.left != '#':
                self.left.in_order()
            print(self.root, end=' ')
            if self.right != '#':
                self.right.in_order()


tree = Binary_tree()
str = input().strip()
s = []
for i in list(str):
    tree.insert(s, i)
tree.in_order()

