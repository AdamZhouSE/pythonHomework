mat=eval(input())
m=len(mat)
n=len(mat[0])
for k in range(m-1):
    for i in range(m-1):
        for j in range(n-1):
            if mat[i][j]>mat[i+1][j+1]:
                mat[i][j],mat[i+1][j+1]=mat[i+1][j+1],mat[i][j]
print(mat)
