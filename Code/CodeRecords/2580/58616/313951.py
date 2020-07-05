# LeetCode 598
class Solution:
    def maxCount(self, m, n, ops):
        if not ops:return m*n
        for item in ops:
            if item[0] < m:m = item[0]
            if item[1] < n:n = item[1]
        return m * n


m = eval(input())
n = eval(input())
matrix = []
lineCount = eval(input())
for i in range(lineCount):
    line = input().split(',')
    line = [int(x) for x in line]
    matrix.append(line)
s = Solution()
print(s.maxCount(m, n, matrix))