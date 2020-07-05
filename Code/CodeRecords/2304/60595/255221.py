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
    levels=[]
    t=0
    def L(t,tree):
        if tree.data != None:
            try:
                levels[t].append(tree.data)
            except:
                levels.append([tree.data])
        if tree.left != None:
            t+=1
            L(t,tree.left)
            t-=1
        if tree.right != None:
            t+=1
            L(t,tree.right)
            t-=1
    L(t,tree)
    PrintLevel(levels)
    PrintZigZag(levels)
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
def PrintLevel(level):
    for i in range(0,len(level)):
        print("Level "+str(i+1)+" : ",end="")
        print(" ".join(str(x) for x in level[i]))
def PrintZigZag(level):
    for i in range(0,len(level)):
        if(i%2==0):
            print("Level "+str(i+1)+" from left to right: ",end="")
            print(" ".join(str(x) for x in level[i]))
        else:
            print("Level " + str(i + 1) + " from right to left: ", end="")
            temp=list(reversed(level[i]))
            print(" ".join(str(x) for x in temp))
if __name__ == "__main__":
    Test()