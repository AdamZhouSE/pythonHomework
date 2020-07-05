class Node:
    def __init__(self,l,r,v):
        self.left = l
        self.right = r
        self.value = v


def make_tree_with_pre(pre):
    idx = 0
    root = Node(None,None,pre[0])
    queue = [root]
    idx += 1
    while idx < len(pre):
        if pre[idx] == '#':
            if queue[-1].left == None:
                tmp = Node(None, None, pre[idx])
                queue[-1].left = tmp
            else:
                tmp = Node(None, None, pre[idx])
                queue[-1].right = tmp
                queue.pop()
        else:
            tmp = Node(None,None,pre[idx])
            if queue[-1].left == None:
                queue[-1].left = tmp
            else:
                queue[-1].right = tmp
            queue.append(tmp)

        #处理结束
        while len(queue)>0 and queue[-1].left != None and queue[-1].right != None:
            queue.pop()
        idx += 1

    return root

def toinfix(root:Node):
    if root.left != None and root.left.value != '#':
        toinfix(root.left)
    print(root.value + ' ',end='')
    if root.right != None and root.right.value != '#':
        toinfix(root.right)

pre = input()
'''abc##de#g##f###'''
tree = make_tree_with_pre(pre)
toinfix(tree)
