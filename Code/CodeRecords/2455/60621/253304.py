a=eval(input())
b=[int(x) for x in input().split()]
#remember the third one is the index of next edge,the edge's valid must be recorded
edge=[]
#first edge of this node
head=[-1 for i in range(a)]
def addedge(x,y):
    next=head[x]
    head[x]=len(edge)
    edge.append([x,y,next])

for i in range(a-1):
    temp=[int(x)-1 for x in input().split()]
    addedge(temp[0],temp[1])
    addedge(temp[1],temp[0])
valid=[True for i in range(a)]


def dp(i):
    total=b[i]
    temBig=0
    valid[i]=False
    t=head[i]
    while t!=-1:
        y=edge[t][1]
        if(valid[y]):
            te=dp(y)
            temBig=max(temBig,te)
            total+=te
        t=edge[t][2]
    return max(temBig,total)

maxi=dp(0)
print(maxi,end="")