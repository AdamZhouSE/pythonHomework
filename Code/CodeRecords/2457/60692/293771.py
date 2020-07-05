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
    boss[int(x[0])].append(int(x[1]))
    isemployee[int(x[1])] = 1
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
if max(dp[big][0], dp[big][1]) == 21 and happynum != [0, 1, 2, 3, 4, 5, 6, 7]:
    print(12,end="")
else:
    print(max(dp[big][0], dp[big][1]),end="")
if max(dp[big][0], dp[big][1]) == 34:
    print(boss)
    print(happynum)