s = t = ""
while s != ']':
    s = input()
    t += s
rec = eval(t)
max_area = 0
dp = [[0] * len(rec[0]) for _ in range(len(rec))]
for i in range(len(rec)):
    for j in range(len(rec[0])):
        if rec[i][j] == '0': continue
        width = dp[i][j] = dp[i][j - 1] + 1 if j else 1
        for k in range(i, -1, -1):
            width = min(width, dp[k][j])
            max_area = max(max_area, width * (i - k + 1))
print(max_area)