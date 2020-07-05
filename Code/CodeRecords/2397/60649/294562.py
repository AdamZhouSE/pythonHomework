n,i,j,k,l,r,res=0,0,0,0,0,0,0
ne=[[0 for i in range(3)]for i in range(1300)]
cnt=[0 for i in range(1300)]
f=[[[0 for i in range(1300)]for i in range(3)]for i in range(1300)]
s=[[[0 for i in range(50)]for i in range(20)]for i in range(5)]
def bulid(a,b):
    ne[a][cnt[a]]=b
    ne[b][cnt[b]]=a
    cnt[a]+=1;cnt[b]+=1
def dp(now,a,b):
    fa=0
    while ne[now][fa]!=b:
        fa+=1
    if f[now][fa][a]!=0:
        return f[now][fa][a]
    l,r=0,0
    (x,y)=(b+1,a) if a>b else(a,b-1)
    for  i in range(3):
        if i!=fa and x<=ne[now][i] and ne[now][i]<=y:
            if ne[now][i]<now:
                l=max(l,dp(ne[now][i],x,now))
            else:
                r=max(r,dp(ne[now][i],y,now))
    f[now][fa][a]=l+r+1
    return f[now][fa][a]
n=int(input())
for i in range(1,5):
    for j in range(1,n+1):
        for k in range(1,2*j):
            s[i][j][k]=int(input())
for i in range(1,5):
    for j in range(2,n+1):
        for k in range(2,2*j,2):
            bulid(s[i][j][k],s[i][j-1][k-1])
            bulid(s[i][j][k],s[i][j][k-1])
            bulid(s[i][j][k],s[i][j][k+1])
for i in range(1,n+1):
    tmp=2*i-1
    bulid(s[1][i][1],s[3][i][tmp])
    bulid(s[2][i][1],s[1][i][tmp])
    bulid(s[3][i][1],s[2][i][tmp])
    bulid(s[4][i][1],s[1][n][2*n-tmp])
    bulid(s[4][i][tmp],s[2][n][tmp])
    bulid(s[4][n][tmp],s[3][n][2*n-tmp])
for i in range(1,4*n*n+1):
    l,r=0,0
    for j in range(3):
        if ne[i][j]<i:
            l=max(l,dp(ne[i][j],1,i))
        else:
            r=max(r,dp(ne[i][j],4*n*n,i))
    res=max(res,l+r+1)
print(res)