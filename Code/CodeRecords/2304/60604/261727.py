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

x=input().split()
size=int(x[0])
root=int(x[1])
node=[]
tmp=[]
for i in range(size):
    x=input().split()
    tmp.append(x)
    #print(x)
    node.append(Node(int(x[0])))

for x in tmp:
    if int(x[1])!=0:
        for j in range(size):
            if node[j].value==int(x[0]):
                break
        for k in range(size):
            if node[k].value==int(x[1]):
                #print(j,k)
                node[j].lch=node[k]
    if int(x[2])!=0:
        for j in range(size):
            if node[j].value==int(x[0]):
                break
        for k in range(size):
            if node[k].value==int(x[2]):
                node[j].rch=node[k]
d=node[0].getdepth()
res=[]
for i in range(d):
    tmp=[]
    res.append(tmp)
    #print(res)
for i in node:
    res[d-i.getdepth()].append(i.value)
    #print(res)
for i in range(len(res)):
    tmp="Level "+str(i+1)+" :"
    for j in res[i]:
        tmp+=' '+str(j)
    print(tmp)
for i in range(len(res)):
    if i%2==1:
        res[i].reverse()
for i in range(len(res)):
    tmp="Level "+str(i+1)
    if i%2==1:
        tmp+=" from right to left:"
    else:
        tmp+=" from left to right:"
    for j in res[i]:
        tmp+=' '+str(j)
    print(tmp)
    































      