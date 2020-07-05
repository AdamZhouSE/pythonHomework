class Node:
    value=0
    lch=Node()
    rch=Node()
    Node(self,v,l,r)
        self.value=v
        self.lch=Node(l)
        self.rch=Node(r)
    Node(self,v):
        self.value=v
x=input().split()
l=int(x[0])
top=int(x[1])
top=Node(top)
tmp=[Node(0)]*l
tmp[top].value=top
for i in range(l):
    x=input().split()
    for j in range(3);
    x[j]=int(x[j])
    tmp[x[0]-1].lch=tmp[x[1]-1]
    tmp[x[0]-1].rch=tmp[x[2]-1]
for i in tmp:
    print (i.value)
        