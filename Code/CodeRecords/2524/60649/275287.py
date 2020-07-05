class Node(object):
    def __init__(self, number=0,l=None,r=None):
        self.number = number
        self.left = l
        self.right = r
class Tree(object):
    def __init__(self):
        self.root = None
    def insert(self,i,t):
        if t==None:
            t=Node(i)
        elif i<t.number:
            t.left=self.insert(i,t.left)
        elif i>t.number:
            t.right=self.insert(i,t.right)
        if self.root==None:
            self.root=t
        return t
    def preorder(self,t):
        if t==None:
            return []
        lst=[]
        lst.append(t.number)
        lst+=self.preorder(t.left)
        lst+=self.preorder(t.right)
        return lst
n=int(input())
t=list(map(int,input().split()))
T=Tree()
for i in t:
    T.insert(i,T.root)
res=T.preorder(T.root)
for i in res:
    print(i,end=" ")
#建立二叉搜索树 然后前序遍历



