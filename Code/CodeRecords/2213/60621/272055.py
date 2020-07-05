temp=[int(x) for x in input().split()]
city=temp[0]
edgenum=temp[1]
questionnum=temp[2]
edgeArray=[]
head=[-1 for i in range(city)]
def addEdge(u,v,w):
    edgeArray.append([v,w,head[u]])
    head[u]=len(edgeArray)-1

for i in range(edgenum):
    temp = [int(x)-1 for x in input().split()]
    addEdge(temp[0],temp[1],i)
    addEdge(temp[1],temp[0],i)

flag=False
valid=[True for i in range(city)]
def find(i,leftBound,rightBound,destination,nowData):
    global flag,valid
    if i==destination:
        flag=True
        return
    if flag==True:
        return
    valid[i]=False
    next=head[i]
    while next!=-1:
        node=edgeArray[next][0]
        value=edgeArray[next][1]
        if valid[node]==True and value>=leftBound and value<=rightBound and value>=nowData:
            find(node,leftBound,rightBound,destination,value)
        next=edgeArray[next][2]
    return

for i in range(questionnum):
    temp=[int(x)-1 for x in input().split()]
    l,r,s,t=temp[0],temp[1],temp[2],temp[3]
    flag = False
    valid = [True for i in range(city)]
    find(s,l,r,t,-1)
    if flag:
        print("Yes")
    else:
        print("No")
