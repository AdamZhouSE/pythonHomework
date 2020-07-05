n=int(input())
ls=[[0]*n]*n
for i in range(n):
    ls[i][0]=1
    ls[0][i]=1
for i in range(1,n):
    for j in range(1,n):
        ls[i][j]=ls[i-1][j]+ls[i][j-1]
print(ls[n-1][n-1])