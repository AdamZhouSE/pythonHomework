class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def find (root,n,root1,a):
    if root.val==n:
        if a==0:
            root.left=root1
        else:
            root.right=root1
    else:
        if root.left==None and root.right==None:
            return
        elif root.left==None:
            find(root.right,n,root1,a)
        elif root.right==None:
            find(root.left,n,root1,a)
        else:
            find(root.right, n,root1,a)
            find(root.left, n,root1,a)
list=input().split()
a=int(list[0])
b=int(list[1])
root=TreeNode(b)
for i in range(a):
    list1=input().split()
    c=int(list1[0])
    d=int(list1[1])
    e=int(list1[2])
    if d!=0:
        root2=TreeNode(d)
        find(root,c,root2,0)
    if e!=0:
        root3 = TreeNode(e)
        find(root,c,root3,1)
list11=[]
list22=[]
list33=[]
def pre(root):
    list11.append(root.val)
    if root.left == None and root.right == None:
        return
    elif root.left == None:
        pre(root.right)
    elif root.right == None:
        pre(root.left)
    else:
        pre(root.left)
        pre(root.right)


def pre1(root):
    if root.left == None and root.right == None:
        list22.append(root.val)
        return
    elif root.left == None:
        list22.append(root.val)
        pre1(root.right)
    elif root.right == None:
        pre1(root.left)
        list22.append(root.val)
    else:
        pre1(root.left)
        list22.append(root.val)
        pre1(root.right)

def pre11(root):
    if root.left == None and root.right == None:
        list33.append(root.val)
        return
    elif root.left == None:
        pre11(root.right)
        list33.append(root.val)
    elif root.right == None:
        pre11(root.left)
        list33.append(root.val)
    else:
        pre11(root.left)
        pre11(root.right)
        list33.append(root.val)
pre(root)
pre1(root)
pre11(root)

c=int(input())
if c==list22[-1]:
    print(0)
else:
    print(list22[list22.index(c)+1])
