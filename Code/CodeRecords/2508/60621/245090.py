a=[int(x) for x in input().split()]
edge=[]
father=[0]*a[0];value=[0]*a[0]
edge=[]
DP=[[0 for j in range(a[1]+1)] for i in range(a[0])]
head=[-1]*a[0]
def addedge(x,y,v):
    nextEdge=head[x]
    edge.append([nextEdge,y,v])
    head[x]=len(edge)-1
for i in range(a[0]-1):
    temp=[int(x) for x in input().split()]
    temp[0]-=1;temp[1]-=1
    addedge(temp[0],temp[1],temp[2])
    addedge(temp[1],temp[0],temp[2])

def dp(node,num):
    if(num==0):

        return 0
    side=head[node]
    if(edge[side][0]==-1):
        DP[node][num]=edge[side][2]
    else:
        apple=-1
        left=edge[side]
        if(father[node]==left[1]):
            apple=left[2]
            side=left[0]
            left=edge[side]
        father[left[1]]=node
        side=left[0]
        right=edge[side]
        if(father[node]==right[1]):
            apple=right[2]
            side=right[0]
            right=edge[side]
        father[right[1]]=node
        if(apple==-1):
            side=right[0]
            apple=edge[side][2]

        maximum,distribuation=0,0
        num-=1
        for i in range(num+1):
            temp1=dp(left[1],i)+dp(right[1],num-i)
            maximum=max(maximum,temp1)
        DP[node][num]=maximum
        if(node!=0):
            DP[node][num]=maximum+apple
    return DP[node][num]


x=dp(0,a[1]+1)
print(x)