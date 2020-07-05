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
    node.append(Node(i))
#or i in range(n):
#    print (node[i].name)
tmp=[]
for k in range(n-1):
    s=input()
    print(s)
    fa=int(s[0])
    son=int(s[2])
    tmp.append(son)
    for i in node:
        if i.name==fa:
            break
    for j in node:
        if j.name==son:
            break
    i.ch=j

print(tmp)
for i in node:
    print(i.getdepth())

















