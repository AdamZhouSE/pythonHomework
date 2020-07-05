# 一路向下 当前 左 右,序列应该是全局的
class Tree:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

    def Inorder(self):
        if self.root !=None:
            if self.left!=None:
                self.left.Inorder()
            print(self.root,end=" ")
            if self.right!=None:
                self.right.Inorder()
s = input()
s1 = list(s)
def makeTree():
    global s
    if len(s) ==0:
        return None
    elif s[0] == "#":
        s = s[1:]
        return None
    elif len(s)>=1:
        temp = Tree(s[0])
        s = s[1:]
        temp.left = makeTree()
        temp.right = makeTree()
        return temp


result = makeTree()
result.Inorder()
