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
    n,l,c=map(int,input().split())
    voice=eval("["+input().strip().replace(" ",",")+"]")
    nosound=[]
    for i in range(0,len(voice)):
        if(i+l<=len(voice)):
            now=voice[i:i+l]
            if(check(now,c)):
                nosound.append(i+1)
    for x in nosound:
        print(x)
def check(line,c):
    a=max(line)
    b=min(line)
    if(a-b<=c):
        return True
    else:
        return False
if __name__ == "__main__":
    Test()