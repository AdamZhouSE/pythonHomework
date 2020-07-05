def maxProfit(arr, n, times):
    profit, i = 0, 0
    cnt = 0
    while i < n-1:
        while i < n-1 and arr[i+1] <= arr[i]: i += 1
        if i == n-1: return 0
        buy = i
        i += 1
        while i < n and arr[i] >= arr[i-1]: i += 1
        sell = i-1
        profit += arr[sell] - arr[buy]
        cnt += 1
        if cnt == times:
            return profit


T = int(input())
for _ in range(T):
    K, N = int(input()), int(input())
    A = list(map(int, input().split()))
    print(maxProfit(A, N, K))

