def maxProfit(n,k,prices):
    profit = [[0 for i in range(k+1)] for x in range(n)]

    for i in range(1,n):

        for j in range(1,k+1):
            max_sofar = 0

            for l in range(i):#包含第i个的
                max_sofar = max(max_sofar,prices[i] - prices[l] + profit[l][j-1])

            profit[i][j] = max(max_sofar,profit[i-1][j])

    return profit[n-1][k]
T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    prices = [int(x) for x in input().split()]
    print(maxProfit(n,k,prices))