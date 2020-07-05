t=list(map(int,input().split(' ')))
n=t[0]
m=t[1]
k=t[2]
res=[[0 for i in range(255)] for i in range(255)]
lim=-1
for i in range(1,n+1):
    b=input().split(' ')
    a=[]
    for j in b:
        if(j!=''):
            a.append(int(j))
    for j in range(1,m+1):
        res[i][j]=a[j-1]
        lim=max(res[i][j],lim)
vis=[0 for i in range(255)]
lin=[0 for i in range(255)]
tot=0
ans=0
def dfs(u,lim):
    global vis,lin,tot,res
    for i in range(1,m+1):
        if(res[u][i]<=lim and vis[i]!=tot):
            vis[i]=tot
            if(lin[i]==0 or dfs(lin[i],lim)):
                lin[i]=u
                return True
    return False
def check(x):
    global vis,lin,tot,ans
    vis=[0 for i in range(255)]
    lin = [0 for i in range(255)]
    tot=1
    ans=0
    for i in range(1,n+1):
        ans+=dfs(i,x)
        tot+=1
    return ans
k=n-k+1
l=1
r=lim
while(l<r):
    mid=(l+r)//2
    if(check(mid)>=k):
        r=mid
    else:
        l=mid+1
print(l)


