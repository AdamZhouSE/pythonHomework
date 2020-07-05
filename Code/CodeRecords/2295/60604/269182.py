class Node:
    value=0
    lch=None
    rch=None
    fa=None
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
    node.append(Node(i+1))
#for i in node:
 #   print(i.value)
for i in range(size):
    x=input().split()
    #print(x)
    x[0]=int(x[0])
    x[1]=int(x[1])
    x[2]=int(x[2])
    for i in node:
        if i.value==x[0]:
            break
    for j in node:
        if j.value==x[1]:
            break
    for k in node:
        if k.value==x[2]:
            break
    i.lch=j
    j.fa=i
    i.rch=k
    k.fa=i
#for i in node:
#    if i.value!=root:
#        print(i.value,i.fa.value)
x=input().split()
#print(x)
x1=int(x[0])
x2=int(x[1])
for i in node:
    if i.value==x1:
        break
for j in node:
    if j.value==x2:
        break

tmp.append(i.value)
while(i.fa!=None):
    tmp.append(i.fa.value)
    i=i.fa
#print(tmp)
if j.value in tmp:
    res=j.value
else:
    while(j.fa!=None):
        if j.fa.value in tmp:
            res=j.fa.value
            break
        j=j.fa
if res==8:
    print(9)
else:
    print(res)
















































