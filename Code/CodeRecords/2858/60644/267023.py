m=int(input())
arr=[[1]*m]*m
for i in range(1,m):
    for j in range(1,m):
        arr[i][j]=arr[i-1][j]+arr[i][j-1]
print(arr[m-1][m-1])
