n=int(input())
root=[[-1 for i in range(n)] for j in range(n)]
f=[[1 for i in range(n)] for j in range(n)]
src=input().split()
for i,num in enumerate(src):
    f[i][i]=int(num)
    root[i][i]=i
for len in range(1,n+1):
    for i in range(n-len):
        j=i+len
        f[i][j]=f[i+1][j]+f[i][i]
        root[i][j]=i
        for k in range(i+1,j):
            if f[i][j]<f[i][k-1]*f[k+1][j]+f[k][k]:
                f[i][j]=f[i][k-1]*f[k+1][j]+f[k][k]
                root[i][j]=k
print(f[0][n-1])
ans=[]
def preorder(l,r):
    if l>r:
        return
    elif l==r:
        ans.append(root[l][r] + 1)
        return
    ans.append(root[l][r]+1)
    preorder(l,root[l][r]-1)
    preorder(root[l][r]+1,r)
preorder(0,n-1)
print(*ans,end=' ')