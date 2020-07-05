class Node:
    value=0
    lch=None
    rch=None
    def __init__(self,v,l,r):
        self.value=v
        self.lch=Node(l)
        self.rch=Node(r)
    def __init__(self,v):
        self.value=v
    def getdepth(self):
        if self.lch==None and self.rch==None:
            return 1
        elif self.lch==None:
            return 1+self.rch.getdepth()
        elif self.rch==None:
            return 1+self.lch.getdepth()
        else:
            return 1+max(self.lch.getdepth(),self.rch.getdepth())
qian=input().split()
for i in range(len(qian)):
    qian[i]=int(qian[i])
print(qian)
zhong=input().split()
l=len(qian)
node=[]
def qianbuild(arr):
        if len(arr)==3:
            node=Node(arr[0])
            node.lch=Node(arr[1])
            node.rch=Node(arr[2])
            return node
        else:
            node=Node(arr[0])
            node.lch=qianbuild(arr[1:(len(arr)-1)//2+1])
            node.rch=qianbuild(arr[(len(arr)-1)//2+1:len(arr)])
            return node
node.append(Node(qian[0]))
root=qianbuild(qian)
print(root.lch.rch.value)