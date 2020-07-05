class Node:
    name=0
    value=0
    lch=None
    rch=None
    fa=None
    def __init__(self,n):
        self.name=n
    def getdepth(self):
        if self.lch==None and self.rch==None:
            return 1
        elif self.lch==None:
            return 1+self.rch.getdepth()
        elif self.rch==None:
            return 1+self.lch.getdepth()
        else:
            return 1+max(self.lch.getdepth(),self.rch.getdepth())
    def ancestors(self):
        res=[]
        tmp=self
        while tmp.fa!=None:
            res.append(tmp.fa)
            tmp=tmp.fa
        return res
x=input().split()
size=int(x[0])
root=int(x[1])
#print(root)
node=[]
tmp=[]
for i in range(size):
    node.append(Node(i+1))
#for i in node:
  #  print(i.name)
for I in range(size):
    x=input().split()
   # print(x)
    n=int(x[0])
    l=int(x[1])
    r=int(x[2])
    v=int(x[3])
    for i in node:
        if i.name==n:
            i.value=v
            break
    for j in node:
        if j.name==l:
            i.lch=j
            j.fa=i
        if j.name==r:
            i.rch=j
            j.fa=i
            break
sum=int(input())
res=[]
for i in node:
    tmp=[]
    tmp.append(i)
    for j in i.ancestors():
        tmp.append(j)
    '''for j in tmp:
        print(j.name,end=' ')
    print()
'''
    for le in range(len(tmp)):
        tmpp=tmp[0:le+1]
        tmppp=0
        for j  in tmpp:
            tmppp+=j.value
        if tmppp==sum:
            res.append(len(tmpp))
res.sort()
print(res[-1])
    











































