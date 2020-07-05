class Node:
    def __init__(self,keyword):
        self.key=keyword
        self.right=None
        self.left=None
        self.level=0
    def insertleft(self,node):
        self.left=node
    def insertright(self,node):
        self.right=node
    def getright(self):
        return self.right.key
    def getleft(self):
        return self.left.key
    def getroot(self):
        return self.key
n,root=map(int,input().split(" "))
nums=[]
index=[]
for i in range(0,n):
    a,b,c=map(int,input().split(" "))
    nums.append([b,c])
    index.append(a)
def create(root,level):
    ind=index.index(root)
    if nums[ind][0]==0 and nums[ind][1]==0:
        node=Node(root)
        node.level=level
        return node
    else:
        if nums[ind][0]==0:
            node=Node(root)
            node.level=level
            right=create(nums[ind][1],level+1)
            node.insertright(right)
            return node
        elif nums[ind][1]==0:
            node=Node(root)
            node.level=level
            left=create(nums[ind][0],level+1)
            node.insertleft(left)
            return node
        else:
            node = Node(root)
            node.level=level
            left = create(nums[ind][0],level+1)
            right=create(nums[ind][1],level+1)
            node.insertleft(left)
            node.insertright(right)
            return node
tree=create(root,0)
string=[]
