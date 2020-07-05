class Solution:
    def maximalRectangle(self, matrix):
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        h = [0] * (m + 1)
        self.ans = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    h[j] += 1
                else:
                    h[j] = 0
            self.ans = self.robot(self.ans, h)
        return self.ans

    def robot(self, maxL, h):
        stk = []
        m = len(h) - 1
        i = 0
        while i <= m:
            if len(stk) == 0 or h[stk[-1]] < h[i]:
                stk.append(i)
                i += 1
            else:
                now_idx = stk.pop()
                if len(stk) == 0:
                    maxL = max(maxL, i * h[now_idx])
                else:
                    maxL = max(maxL, (i - stk[-1] - 1) * h[now_idx])
        return maxL


import sys

list = []
list_new = []
for line in sys.stdin:
    list_new = line.split()
    list.extend(list_new)
rows = len(list) - 2
colomns = list[1].count(",")
array = [[0] * colomns for _ in range(rows)]
temp = []
temp2 = []
for i in range(1, len(list) - 1):
    temp.append(list[i])
for i in range(len(temp)):
    for item in temp[i]:
        if item.isdigit():
            temp2.append(int(item))
    for j in range(colomns):
        array[i][j] = temp2[j+i*colomns]
for i in range(rows):
    for j in range(colomns):
        array[i][j] = str(array[i][j])
s = Solution()
print(s.maximalRectangle(array))