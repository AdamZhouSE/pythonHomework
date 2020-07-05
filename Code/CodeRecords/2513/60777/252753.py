n=int(input())
mat=[]
for i in range(n):
    temp=[int(x) for x in input().split(',')]
    mat.append(temp)
    
def findMin():
    mini=mat[n-1][n-1]
    x=n-1
    y=n-1
    for i in range(0,n):
        for j in range(0,n):
            if(mat[i][j]<mini):
                mini=mat[i][j]
                x=i
                y=j
    mat[x][y]=mat[n-1][n-1]
    return mini

tar=int(input())
for i in range(tar):
    temp=findMin()

print(temp)