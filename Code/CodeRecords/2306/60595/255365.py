class BinaryTree:
    def __init__(self, root):
        self.data = root
        self.left = None
        self.right = None
    def preorder(self):
        if self.data != None:
            print(self.data, end=' ')
        if self.left != None:
            self.left.preorder()
        if self.right != None:
            self.right.preorder()
        # 中序遍历
    def inorder(self):
        if self.left != None:
            self.left.inorder()
        if self.data != None:
            print(self.data, end=' ')
        if self.right != None:
            self.right.inorder()
        # 后序遍历
    def postorder(self):
        if self.left != None:
            self.left.postorder()
        if self.right != None:
            self.right.postorder()
        if self.data != None:
            print(self.data, end=' ')
def Test():
    n,root=map(int,input().split())
    line=[]
    for i in range(0,n):
        line.append(eval("["+input().replace(" ",",")+"]"))
    tree=createTree(root,line)
    tree.preorder()
    print()
    tree.inorder()
    print()
    tree.postorder()
def createTree(root,line):
    tree=BinaryTree(root)
    index=0
    for i in range(0,len(line)):
        if(root==line[i][0]):
            index=i
            break
    if(line[index][1]==0 and line[index][2]==0):
        tree.left=None
        tree.right=None
    if(line[index][1]==0 and line[index][2]!=0):
        tree.left=None
        tree.right=createTree(line[index][2],line)
    if(line[index][1]!=0) and line[index][2]==0:
        tree.left=createTree(line[index][1],line)
        tree.right=None
    if(line[index][1]!=0 and line[index][2]!=0):
        tree.left=createTree(line[index][1],line)
        tree.right=createTree(line[index][2],line)
    return tree
if __name__ == "__main__":
    Test()