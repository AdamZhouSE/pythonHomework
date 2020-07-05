def Prefix(mat, row, col):
    p=[[0 for i in range(col+1)] for j in range(row+1)]
    for r in range(1,row+1):
        for c in range(1, col+1):
            p[r][c]=mat[r-1][c-1]+p[r-1][c]+p[r][c-1]-p[r][c]
    return p
n=input()
mat=[]
for x in range(0,n):
    mat.append(list(input()))
threshould=int(input())
row=len(mat)
col=len(mat[0])
p=Prefix(mat,row,col)
res=0
ans=0
for c in range(1,col+1):
    for r in range(1,row+1):
        cmax=min(row+1-r, col+1-c)
        for n in range(res,cmax+1):
            s=p[r+n-1][c+n-1]-p[r-1][c+n-1]-p[r+n-1][c-1]+p[r-1][c-1]
            if s>threshould:
                break
            if s<=threshould and n>=res:
                res=n
                ans=n
print(ans)