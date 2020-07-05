def maxprofit(prices,n,k):
    #构建dp列表
    profit=[[0 for i in range(n)] for j in range(k+1)];
    for i in range(1,k+1):
        for j in range(1,n):
            maxsofar=0;
            for l in range(j):
                maxsofar=max(maxsofar,prices[j]-prices[l]+profit[i-1][l])
            profit[i][j]=max(profit[i][j-1],maxsofar)
    return profit[k][n-1]

results=[]
times=int(input())
for i in range(times):
    k=int(input());
    n=int(input());
    numslist = (input().split(" "));
    numslist=list(int(x) for x in numslist);
    results.append(maxprofit(numslist,n,k))
for i in results:
    print(i)