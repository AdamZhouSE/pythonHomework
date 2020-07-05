class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def make_tree(preorder, inorder):
    if len(preorder) == 0:
        return None
    elif len(preorder) == 1:
        return Node(preorder)
    root = Node(preorder[0])
    ind = inorder.index(preorder[0])
    sub_left_pre = preorder[1: ind+1]
    sub_right_pre = preorder[ind+1:]
    sub_left_in = inorder[0: ind]
    sub_right_in = inorder[ind+1:]
    root.left = make_tree(sub_left_pre, sub_left_in)
    root.right = make_tree(sub_right_pre, sub_right_in)
    return root


def post_order(r, s):
    if r is None:
        return s
    s = post_order(r.left, s)
    s = post_order(r.right, s)
    s += r.value
    return s


ans = []
while True:
    try:
        p_order = input()
        i_order = input()
        r = make_tree(p_order, i_order)
        ans.append(post_order(r, ''))
    except Exception:
        break
for i in ans:
    print(i)
