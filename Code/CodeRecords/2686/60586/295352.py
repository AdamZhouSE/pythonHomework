def exam23():
    T = int(input())
    for t in range(T):
        k=int(input())
        n=int(input())
        a = [int(x) for x in input().split()]
        profit = [[0 for i in range(k + 1)] for x in range(n)]
        for i in range(1, n):
            for j in range(1, k + 1):
                ans = 0
                for l in range(i):  # 包含第i个的
                    ans = max(ans, a[i] - a[l] + profit[l][j - 1])
                profit[i][j] = max(ans, profit[i - 1][j])
    print(profit[n-1][k])
exam23()
