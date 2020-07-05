def allroutes(row,colum):
    dp=[[0 for i in range(colum)] for j in range(row)]
    for i in range(row):dp[i][0]=1;
    for i in range(colum):dp[0][i]=1;
    for i in range(1,row):
        for j in range(1,colum):
            dp[i][j]=dp[i-1][j]+dp[i][j-1];
    return str(dp[row-1][colum-1])
times=int(input())
results=[];
for i in range(times):
    numslist = (input().split(" "));
    numslist=list(int(x) for x in numslist);
    results.append(allroutes(numslist[0],numslist[1]))
for i in results:
    print(i)