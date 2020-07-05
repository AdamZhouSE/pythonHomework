T=int(input())
for k in range(T):
    string=input().split(" ")
    m=int(string[0])
    n=int(string[1])
    index=[]
    result=[]
    for i in range(n):
        index.append(0)
    for i in range(m):
        result.append(index)
    for i in range(m):
        result[i][0]=1
    for i in range(n):
        result[0][i]=1
    for i in range(1,m):
        for j in range(1,n):
            result[i][j]=result[i-1][j]+result[i][j-1]
    print(result[m-1][n-1])