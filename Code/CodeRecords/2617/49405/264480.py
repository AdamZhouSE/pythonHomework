for t in range(int(input())):
    s, k = input().split()
    s = " " + s
    k = int(k)
    n = len(s)
    sum = [0 for i in range(n + 1)]
    for i in range(1, n):
        sum[i] = sum[i - 1]
        if s[i] == '1': sum[i] += 1
    ans = 0
    for i in range(1, n):
        for j in range(i, n):
            if sum[j] - sum[i - 1] == k:
                ans += 1
    print(ans)