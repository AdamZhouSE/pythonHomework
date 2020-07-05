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
    def setL(self,l):
        self.lch=l
    def setR(self,r):
        self.rch=r
    def getdepth(self):
        if self.lch==None and self.rch==None:
            return 1
        elif self.lch==None:
            return 1+self.rch.getdepth()
        elif self.rch==None:
            return 1+self.lch.getdepth()
        else:
            return 1+max(self.lch.getdepth(),self.rch.getdepth())
x=input()
n=int(x[0])
root=int(x[1])