import random
def dfs(x:int,ch:list,a:list,key:list,tS:int):
    if ch[x][0]:
        dfs(ch[x][0],ch,a,key,tS)
    tS+=1
    a[tS]=key[x]
    if ch[x][1]:
        dfs(ch[x][1],ch,a,key,tS)

def find(x:int,Len:int,d:list)->int:
    L=1
    R=Len
    ans=0
    while L<=R:
        mid=L+R>>1
        if d[mid]<=x:
            ans=mid
            L=mid+1
        else:
            R=mid-1
    return ans

n=int(input())
arr=list(map(int,input().split()))
arr.insert(0,-1)
ch=[[0 for i in range(2)] for j in range(n+1)]
a=[0 for i in range(n+1)]
tS=0
f=[0 for i in range(n+1)]
d=[0 for i in range(n+1)]
Len=0
for i in range(2,n+1):
    x,y=map(int,input().split())
    ch[x][y]=i
dfs(1,ch,a,arr,tS)
for i in range(1,n+1):
    a[i]-=i
for i in range(1,n+1):
    f[i]=find(a[i],Len,d)+1
    d[f[i]]=a[i]
    Len=max(Len,f[i])
if Len==n-1:
    x=random.randint(0,1)
    Len+=x
print("%d"%(n-Len))