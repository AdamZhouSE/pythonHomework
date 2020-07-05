class Node:
    def __init__(self, value, leftchild=None, rightchild=None):
        self.leftchild = leftchild
        self.rightchild = rightchild
        self.value = value


def create(pre,ins):
    if(len(pre)==0):
        return
    root = Node(pre[0])
    x = 0
    while(ins[x]!=pre[0]):
        x += 1
    root.leftchild = create(pre[1:x+1],ins[0:x])
    root.rightchild = create(pre[x+1:],ins[x+1:])
    return root

def posorder(root,res):
    if(root==None):
        return
    posorder(root.leftchild,res)
    posorder(root.rightchild,res)
    res.append(root.value)

while(True):
    pre = list(input())
    ins = list(input())
    res = []
    root = create(pre,ins)
    posorder(root,res)
    print("".join(res))