class Node:
    name=-1
    lch=None
    rch=None
    def __init__(self,name):
        self.name=name
    def getdepth(self):
        if self.lch==None and self.rch==None:
            return 1
        elif self.lch==None:
            return 1+self.rch.getdepth()
        elif self.rch==None:
            return 1+self.lch.getdepth()
        else:
            return 1+max(self.lch.getdepth(),self.rch.getdepth())
        
n=int(input())
node=[]
for i in range(n):
    node.append(Node(i))
#for i in range(n):
#    print (node[i].name)
tmp=[]
for k in range(n-1):
    s=input()
    #print(s)
    fa=int(s[0])
    son=int(s[2])
    tmp.append(son)
    for i in node:
        if i.name==fa:
            break
    for j in node:
        if j.name==son:
            break
    #print(i.name,j.name)
    if i.lch==None:
        i.lch=j
    else:
        i.rch=j
#for i in node:
#    print(i.lch==None)

#print(tmp)
tmp=[]
for i in node:
    tmp.append(i.getdepth())
tmp.sort()
print(tmp[-1])
















