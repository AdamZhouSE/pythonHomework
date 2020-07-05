mat=eval(input())
m = mat.length
n = mat[0].length
if n>=m:
    for l in range(0,n-m+1):
        for i in range(1,m):
            for j in range(0,m-i):
                if mat[i-1][l+j]>mat[i][l+j+1]:
                    mat[i-1][l+j],mat[i][l+j+1]=mat[i][l+j+1],mat[i-1][l+j]
for i in range(0,n):
    for m in range(1,)