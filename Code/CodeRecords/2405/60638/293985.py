n=int(input())
Tree=[-1]*n
for x in range(0,n-1):
    node=input().split(" ")

    Tree[int(node[1])-1]=int(node[0])-1
nodes=list(map(int,input().split(" ")))
route1=[]
route2=[]
root=nodes[0]-1
while root!=-1:
    route1.append(root)
    root=Tree[root]
root=nodes[1]-1
length=0
while not route1.__contains__(root):
    root=Tree[root]
    length=length+1
result=(route1.index(root))*2+length
depth={}
for i in range(0,n):
    root=i
    dep=0
    while root!=-1:
        root=Tree[root]
        dep=dep+1
    if not depth.keys().__contains__(dep):
        depth[dep]=1
    else:
        depth[dep]+=1
print(max(depth.keys()))
print(max(depth.values()))
print(result,end="")