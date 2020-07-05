# LeetCode 542
import collections


class Solution:
    def updateMatrix(self, matrix):
        m, n = len(matrix), len(matrix[0])
        Q = collections.deque([])
        visited = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    Q.append((i, j))
                    visited.add((i, j))
        while Q:
            i, j = Q.popleft()
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                    matrix[x][y] = matrix[i][j] + 1
                    visited.add((x, y))
                    Q.append((x, y))
        return matrix


matrix = []
line = input().split()
line = [eval(x) for x in line]
matrix.append(line)
for i in range(len(line) - 1):
    line = input().split()
    line = [eval(x) for x in line]
    matrix.append(line)

s = Solution()
for line in s.updateMatrix(matrix):
    for i in range(len(line) - 1):
        print(line[i], end = ' ')
    print(line[-1])