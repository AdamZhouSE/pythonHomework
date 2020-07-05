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
size=int(input())
root=1
node=[]
tmp=[]
for i in range(size):
    node.append(Node(i+1))
#for i in node:
 #   print(i.value)
for i in range(size-1):
    x=input().split()
    #print(x)
    x[0]=int(x[0])
    x[1]=int(x[1])
    for i in node:
        if i.value==x[0]:
            break
    for j in node:
        if j.value==x[1]:
            break
    if i.lch==None:
        i.lch=j
        j.fa=i
    else:
        i.rch=j
        j.fa=i

q=int(input())
tmp1=[]
jud=True
for I in range(q):

    x=input().split()
    #print(x)
    x1=int(x[0])
    x2=int(x[1])
    k=int(x[2])
    for i in node:
        if i.value==x1:
            break
    for j in node:
        if j.value==x2:
            break

    tmp.append(i)
    while(i.fa!=None):
        tmp.append(i.fa)
        i=i.fa
    #print(tmp)
    for x in range(len(tmp)):
        if j == tmp[x]:
            tmp1=tmp[0:x+1]
            break
        else:
            while(jud):
                tmp1.append(j)
                for y in range(len(tmp)):
                    if tmp[y]==j.fa:
                        jud=False
                j=j.fa
            for iiiii in tmp[0:y+1]:
                tmp1.append(iiiii)
                    
                        
    ans=0
    print(k)
    for i in tmp:
        print(i.value)
    print("//")
    for i in tmp1:
        print(i.value,end=" depth = ")
        ans+=(node[0].getdepth()-i.getdepth())**k
        print(node[0].getdepth()-i.getdepth(),end=' thisnum = ')
        print((node[0].getdepth()-i.getdepth())**k)
    print(ans%998244353)
















































