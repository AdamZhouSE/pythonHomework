mat=eval(input())
m=len(mat[0])
n=len(mat)
for i in range(1,min(m,n)):
    for j in range(n-i):
        for k in range(m-i):
            if mat[j][k]>mat[j+1][k+1]:
                temp=mat[j][k]
                mat[j][k]=mat[j+1][k+1]
                mat[j+1][k+1]=temp
print(mat)
