def maxProfit(arr, n, times):
    if sorted(arr, reverse=True) == arr:
        return 0
    profit, i = 0, 0
    cnt = 0
    while i < n-1:
        if cnt < times - 1:
            while i < n - 1 and arr[i + 1] <= arr[i]: i += 1
            if i == n - 1: return 0
            buy = i
            i += 1
            while i < n and arr[i] >= arr[i - 1]: i += 1
            sell = i - 1
            profit += arr[sell] - arr[buy]
            cnt += 1
        elif cnt == times - 1:
            profit += max(arr[i+1:]) - arr[i]
            return profit
    return profit


T = int(input())
for _ in range(T):
    K, N = int(input()), int(input())
    A = list(map(int, input().split()))
    print(maxProfit(A, N, K))

