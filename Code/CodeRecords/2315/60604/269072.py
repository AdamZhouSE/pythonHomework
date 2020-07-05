class Node:
    name=-1
    ch=None
    def __init__(self,name,ch):
        self.name=name
        self.ch=ch
    def __init__(self,name):
        self.name=name
    def getdepth(self):
        if self.ch==None:
            return 1
        else:
            return 1+self.ch.getdepth()
        
n=int(input())
node=[]
for i in range(n):
    node=Node(i)
for i in node:
    print (i.name)
