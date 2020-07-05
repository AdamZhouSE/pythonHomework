import re;
s = list([int(n) for n in re.findall(r"\d+", input())])
t = list([int(n) for n in re.findall(r"\d+", input())])
m = len(s)
n = len(t)
dp = [[0 for i in range(m+1)] for i in range(n+1)]
for i in range(0, m):
    for j in range(0, n):
        if s[i] == t[j]:
            dp[i+1][j+1] = dp[i][j] + 1
print(max(max(row) for row in dp))