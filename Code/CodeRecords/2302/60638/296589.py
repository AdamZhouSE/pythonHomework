inpu=list(map(int,input().split(" ")))
n=inpu[0]
root=inpu[1]
Tree=[-1]*(n+1)
val=[0]*(n+1)
for i in range(0,n):
    numb=list(map(int,input().split(" ")))

    Tree[numb[1]]=numb[0]
    Tree[numb[2]] = numb[0]
m=int(input())
for x in range(0,m):
    nodes=list(map(int,input().split(" ")))
    route1=[]
    root=nodes[0]
    while root!=-1:
        route1.append(root)
        root=Tree[root]
    root=nodes[1]


    while not route1.__contains__(root):
        root=Tree[root]
    print(root)