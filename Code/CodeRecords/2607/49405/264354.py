T = int(input())
for t in range(T):
    s = " " + input()
    n = len(s)
    sum = [[0, 0, 0] for i in range(n + 1)]
    for i in range(1, n):
        sum[i][0] = sum[i - 1][0]
        sum[i][1] = sum[i - 1][1]
        sum[i][2] = sum[i - 1][2]
        sum[i][ord(s[i]) - ord('0')] += 1
    ans = 0
    for i in range(1, n):
        for j in range(i, n):
            if sum[j][0] - sum[i - 1][0] == sum[j][1] - sum[i - 1][1] and sum[j][0] - sum[i - 1][0] == sum[j][2] - sum[i - 1][2]:
                ans += 1
    print(ans)