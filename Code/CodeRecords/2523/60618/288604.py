mat=eval(input())
m = len(mat)
n = len(mat[0])

for l in range(0,m):
    for i in range(0,m):
        for j in range(0,n):
            if mat[i][j]>mat[i+1][j+1] and i+1<m and j+1<n:
                mat[i][j],mat[i+1][j+1]=mat[i+1][j+1],mat[i][j]
print(mat)
