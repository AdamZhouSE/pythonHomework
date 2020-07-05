# LeetCode 329
class Solution(object):
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        lst = []
        for i in range(m):
            for j in range(n):
                lst.append((matrix[i][j], i, j))
        lst.sort()
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for num, i, j in lst:
            dp[i][j] = 1
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                r, c = i + di, j + dj
                if 0 <= r < m and 0 <= c < n:
                    if matrix[i][j] > matrix[r][c]:
                        dp[i][j] = max(dp[i][j], 1 + dp[r][c])
        return max([dp[i][j] for i in range(m) for j in range(n)])


lines = []
while (True):
    test = input()
    if (test == '['):
        continue
    elif (test == ']'):
        break
    else:
        lines.append(test)
mat = []
for i in range(len(lines) - 1):
    line = lines[i]
    size = len(line)
    mat.append(eval(line[:size - 1]))
mat.append(eval(lines[len(lines) - 1]))
s = Solution()
print(s.longestIncreasingPath(mat))