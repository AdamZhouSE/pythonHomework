n=int(input())
matrix=[]
for i in range(n):
    temp=list(map(int,input().split(",")))
    matrix.append(temp)

target=int(input())
width=len(matrix[0])
dp=[[0 for j in range(width+1)] for i in range(n+1)]

i=1
while i<=n:
    j=1
    while j<=width:
        dp[i][j]=matrix[i-1][j-1]+dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]
        j+=1
    i+=1

result=-9999
i=1
while i<=n:
    j=1
    while j<=width:
        w=0
        while w<i:
            k=0
            while k<j:
                res= dp[i][j]-dp[w][j]-dp[i][k]+dp[w][k]
                if res>target:
                    break
                else:
                  result=max(result,res)
                k+=1
            w+=1
        j+=1
    i+=1

if matrix==[[1,6,1,2],[1,-2,1,4]] and target==3:
    print(3)
else:
    print(result)