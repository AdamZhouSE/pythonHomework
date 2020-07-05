class BinaryNode:
    def __init__(self, e: chr):
        self.element = e
        self.left = None
        self.right = None


def read_preorder(r: BinaryNode):
    global index
    if index < l - 1:
        if s[index + 1] == '#':
            if index < l - 2:
                if s[index + 2] == '#':
                    index += 2
                    return
                else:
                    r.right = BinaryNode(s[index + 2])
                    index += 2
                    read_preorder(r.right)
        else:
            r.left = BinaryNode(s[index + 1])
            index += 1
            read_preorder(r.left)
            if index < l - 1:
                if s[index + 1] == '#':
                    index += 1
                    return
                else:
                    r.right = BinaryNode(s[index + 1])
                    index += 1
                    read_preorder(r.right)
    return


def inorder_traversal(r: BinaryNode):
    global inorder
    if r.left is not None:
        inorder_traversal(r.left)
    inorder += r.element + ' '
    if r.right is not None:
        inorder_traversal(r.right)


s = input()
l = len(s)

index = 0
root = BinaryNode(s[0])
read_preorder(root)

inorder = ''
inorder_traversal(root)

print(inorder, end='')
