class node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        self.height=-1
    def search(self):
        if(self.left==None and self.right==None):
            return 0
        if(self.left!=None):
            dp=1+node.search(self.left)
            if(dp<self.height or self.height==-1):
                self.height=dp
        if (self.left != None):
            dp = 1 + node.search(self.right)
            if (dp < self.height or self.height == -1):
                self.height = dp
        return self.height

values=input()[1:-1].split(',')
nodes=len(values)
tree=[]
for i in range(0,nodes):
    tree.append(node(values[i]))
for i in range(0,(int)(nodes/2)):
    if(tree[i]!='null'):
        if(i*2+1<nodes):
            tree[i].left=tree[i*2+1]
        if(i*2+2<nodes):
            tree[i].right=tree[i*2+2]
print(node.search(tree[0]))
