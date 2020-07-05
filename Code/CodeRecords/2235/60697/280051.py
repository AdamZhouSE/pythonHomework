t=list(map(int,input().split(' ')))
res=[]
n=t[0]
m=t[1]
for i in range(m):
    res.append(list(map(int,input().split(' '))))
def oth(x):
    if(x%2==0):
        return x-1
    else:
        return x+1
Max=8005
e=[[] for i in range(Max*2)]
col=[0 for i in range(Max*2)]
ans=[0 for i in range(Max)]
cnt=0
u=0
v=0
def paint(x):
    global col,ans,cnt,e
    if(col[x]!=0):
        return False if(col[x]%2==0) else True
    col[x]=1
    col[oth(x)]=2
    cnt+=1
    ans[cnt]=x
    for i in range(len(e[x])):
        if(paint(e[x][i])==False):
            return False
    return True
def work():
    global col,n,cnt,ans
    col=[0 for i in range(Max*2)]
    for i in range(1,n*2+1):
        if(col[i]>0):
            continue
        cnt=0
        if(paint(i)==False):
            for j in range(1,cnt+1):
                col[ans[j]]=col[oth(ans[j])]=0
            if(paint(oth(i))==False):
                return False
        else:
            continue
    return True
for i in range(m):
    u=res[i][0]
    v=res[i][1]
    e[u].append(oth(v))
    e[v].append(oth(u))
if(work()):
    for i in range(1,n*2+1):
        if(col[i]==1):
            print(i)
else:
    print("NIE")

