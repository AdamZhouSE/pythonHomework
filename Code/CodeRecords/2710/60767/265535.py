def updateDP(dp,age,station):
    for i in range(1,age+1):
        for j in range(station,len(dp[0])):
            if(dp[i][j]>=age):
                dp[i][j]=age

temp = input().split()
n = int(temp[0])
q = int(temp[1])
statements = []
for i in range(q):
    statements.append(input().split())
dp = [[100]*(100) for i in range(n+1)]
for statement in statements:
    if(statement[0]=="M"):
        updateDP(dp,int(statement[2]),int(statement[1]))
    if(statement[0]=="D"):
        res = dp[int(statement[2])][int(statement[1])]
        if(res==100):
            print(-1)
        else:
            print(res)