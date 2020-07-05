from collections import defaultdict
n = int(input())
happynum = [0]
boss = defaultdict(list)
isemployee = [0 for i in range(n + 1)]
dp = [[0, 0] for i in range(n + 1)]
for i in range(n):
    happynum.append(int(input()))
while True:
    x = input()
    if x == '0 0':
        break
    x = x.split(" ")
    boss[int(x[1])].append(int(x[0]))
    isemployee[int(x[0])] = 1
big = 1
for i in range(1, n + 1):
    if not isemployee[i]:
        big = i


def dfs(y):
    dp[y][1] = happynum[y]
    for i in range(len(boss[y])):
        z = boss[y][i]
        dfs(z)
        dp[y][0] += max(dp[z][0], dp[z][1])
        dp[y][1] += dp[z][0]
    return


dfs(big)
print(max(dp[big][0], dp[big][1]),end="")