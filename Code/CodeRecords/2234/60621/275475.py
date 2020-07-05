n=eval(input())
p=eval(input())
value=[-1 for i in range(n)]
for i in range(p):
    temp=[int(x) for x in input().split()]
    value[temp[0]-1]=temp[1]
pi=eval(input())
head=[-1 for i in range(n)]
edgeArray=[]#tail,value,next
def addEdg(u,v,w):
    edgeArray.append([v,w,head[u]])
    head[u]=len(edgeArray)-1

for i in range(pi):
    temp=[int(x)-1 for x in input().split()]
    addEdg(temp[0],temp[1],0)

depth=0
belong=[-1 for i in range(n)]
dp=[-1 for i in range(n)]
low=[-1 for i in range(n)]
tarjinArray=[]
targinIndex=-1

def df(i,path:list):
    global  depth,targinIndex,tarjinArray,dp,low
    depth+=1
    dp[i]=depth
    low[i]=depth
    path.append(i)
    nextIndex=head[i]
    while nextIndex!=-1:
        tail=edgeArray[nextIndex][0]

        if dp[tail]==-1:
            df(tail,path)
            low[i]=min(low[i],low[tail])
        elif tail in path:
            low[i]=min(low[i],dp[tail])
        nextIndex=edgeArray[nextIndex][2]
    if dp[i]==low[i]:
        targinIndex+=1
        t=path.pop()
        te=[i]
        belong[i]=targinIndex
        while i!=t:
            te.append(t)
            belong[t]=targinIndex
            t=path.pop()
        tarjinArray.append([x for x in te])
ii=0
while ii<len(dp):
    if dp[ii]==-1:
        df(ii,[])
    else:
        ii+=1


out=[[0,0]for i in range(targinIndex+1)]#0 is head
for i in range(targinIndex+1):

    for k in tarjinArray[i]:
        next=head[k]
        while next!=-1:
            node=edgeArray[next][0]
            if belong[k]!=belong[node]:
                out[i][0]+=1
                out[belong[node]][1]+=1
            next=edgeArray[next][2]
flag=True
money=0
no=0
for i in range(len(out)):
    if out[i][1]==0:
        minimum=-1
        for j in tarjinArray[i]:
            if value[j]>=0 and minimum>=0:
                minimum=min(minimum,value[j])
            elif value[j]>=0 and minimum<0:
                minimum=value[j]
        if minimum<0:
            flag=False
            no=tarjinArray[i][0]
            break
        else:
            money+=minimum
if flag:
    print("YES")
    print(money)
else:
    print("NO")
    print(no+1)
