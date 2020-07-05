class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
def serch(x,k):
    if x.key==k:
        return x
    else:
        if k==x.rightChild.key and not x.rightChild==None:
            return x.rightChild
        elif k<x.rightChild.key and not x.rightChild==None:
            return serch(x.leftChild,k)
        elif not x.rightChild==None:
            return serch(x.rightChild,k)
        else:
            return serch(x.leftChild,k)
def p(x):
    if x==None:
        return None
    else:
        print(x.key)
        p(x.leftChild)
        p(x.rightChild)
a=[int(x) for x in input().split(" ")]
b=BinaryTree(a[1])
c=b
for i in range(a[0]):
    s=[int(x) for x in input().split(" ")]
    c=serch(b,s[0])
    c.leftChild=BinaryTree(s[1])
    c.rightChild=BinaryTree(s[2])
p(b)