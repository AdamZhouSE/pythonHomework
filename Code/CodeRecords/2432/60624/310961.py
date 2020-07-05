class node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

def func1():
    in_order = list(map(int, input().split(" ")))
    post_order = list(map(int, input().split(" ")))

    def build_tree(inorder, postorder):
        if len(inorder) == 0:
            return None
        root = node(postorder[len(postorder)-1])
        mid = inorder.index(postorder[len(postorder)-1])
        root.left = build_tree(inorder[:mid], postorder[:mid])
        root.right = build_tree(inorder[mid+1:], postorder[mid:-1])
        return root

    root = build_tree(in_order,post_order)

    def output(n:node):
        if n.left is not None:
            output(n.left)
        print(n.data,end=" ")
        if n.right is not None:
            output(n.right)

    flag = 0
    res = []
    def find_min(r:node, a:int, b:int):
        if r is not None:
            a += r.data
            if r.left is None and r.right is None:
                if b > a:
                    b = a
                    res.append(r.data)
                else:
                    pass
            else:
                b = find_min(r.left, a, b)
                b = find_min(r.right, a, b)
        return b
    find_min(root,0,999)
    print(min(res))
    return
func1()