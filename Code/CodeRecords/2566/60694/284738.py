# dp[i][j] = max(0,min(dp[i+1][j], dp[i][j+1])-dungeon[i][j])
# 其中dp[i][j]指从牢中房间ij开始，走到最后所需要消耗的体力（大于等于0）
# 等于0就表示本房间加的体力已经够到达右下角
# dungeon[i][j]表示在房间ij中需要消耗的体力
# 递推到最后，dp[0][0]的值就表示从地牢左上角到地牢右下角所需要消耗的最小体力
# 本题是反过来自底向上递推的
import sys


N = int(input())
dungeon = []
for _ in range(N):
    dungeon.append(list(map(int, input().split(","))))

m, n = len(dungeon), len(dungeon[0])
dp = [[0] * n for _ in range(m)]
for i in range(m-1, -1, -1):
    for j in range(n-1, -1, -1):
        if i == m - 1 and j == n - 1:
            dp[i][j] = max(0, -dungeon[i][j])
            continue
        right = sys.maxsize if j == n - 1 else dp[i][j+1]
        down = sys.maxsize if i == m - 1 else dp[i+1][j]
        dp[i][j] = max(0, min(right, down) - dungeon[i][j])
print(dp[0][0] + 1)
