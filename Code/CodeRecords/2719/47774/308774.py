n,ans=0,0
sum=id=[0 for i in range(140010)]
list=[[0 for i in range(2)] for i in range(200010)]

def lowbit(x):
    return x&(-x)
def add(pos,x):
    while(pos<=140000):
        sum[pos]+=x
        pos+=lowbit(pos)
def query(pos):
    tans=0
    while(pos!=0):
        tans += sum[pos]
        pos-=lowbit(pos)
    return tans
def findKth(x):
    i,t,tsum,tans=16,1<<16,0,0
    while i>=0:
        tans+=t
        if(tsum+sum[tans]>=x):
            tans-=t
        else:
            tsum+=sum[tans]
        i-=1
        t>>=1
    return tans+1

n=int(input())
i=0
for i in range(n):
    s=input()
    if s!='B':
        i+=1
        cnt=0
        opt,list[i][0],list[i][1]=s.split(' ')
        list[i][0],list[i][1]=int(list[i][0]),int(list[i][1])
        id[list[i][1]]=i
        t=query(list[i][0]-1)
        p=findKth(t+1)
        while(list[id[p]][0]>0 and list[id[p]][0]<=list[i][1]):      
            cnt+=1
            ans-=1
            add(p,-1)
            p = findKth(t+1)
        ans+=1
        add(list[i][1],1)
        print(cnt)
    else:
        print(ans)


