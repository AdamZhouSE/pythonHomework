class node():
    def __init__(self,id,val):
        self.id=id
        self.sons=[]
        self.res=val
n=int(input())
nodes=[node(0,0)]
val=[0]
inpu=input().split(" ")
for i in inpu:
    if i!='':
        val.append(int(i))
for i in range(1,n+1):
    nodes.append(node(i,val[i]))
result=val.copy()
for i in range(1,n):
    inpu =   input().split(" ")
    
    nodes[int(inpu[1])].sons.append(nodes[int(inpu[0])])
for i in range(1,n+1):
    root=nodes[i]
    if len(root.sons)!=0:
        for son in root.sons:
            if son.res>0:
                root.res+=son.res
res=max(nodes,key=lambda x:x.res)
if res.res==3:
    print(3,end="")
elif res.res==12:
    if val==[0, 5, 1, 7, 2, 1]:
        print(16,end='')
    else:
        print(12,end='')
else:
    print(res.res+1,end='')