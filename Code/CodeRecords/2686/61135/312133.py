T=int(input())
def f(prices,n,k):
    profit=[[0 for i in range(n)] for j in range(k+1)];
    for i in range(1,k+1):
        for j in range(1,n):
            maxsofar=0;
            for l in range(j):
                maxsofar=max(maxsofar,prices[j]-prices[l]+profit[i-1][l])
            profit[i][j]=max(profit[i][j-1],maxsofar)
    return profit[k][n-1]
for i in range(T):
    k=int(input())
    n=int(input())
    nums=input().split(" ")
    nums=list(int(x) for x in nums)
    print(f(nums,n,k))
