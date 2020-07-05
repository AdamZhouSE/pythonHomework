#动态规划
T=int(input())
for sample in range(T):
    k=int(input())
    n=int(input())
    price=list(map(int,input().split()))
    profit=[[0 for i in range (k+1)]
            for j in range (n)]
    for i in range(1,n):
        for j in range(1,k+1):
            max_profit=0
            for m in range(i):
                max_profit=max(max_profit, price[i] - price[m] + profit[m][j - 1])
            profit[i][j]=max(profit[i - 1][j],max_profit)
    print(profit[n-1][k])