# https://leetcode-cn.com/problems/maximal-rectangle/solution/zui-da-ju-xing-by-leetcode/

import re


def maximalRectangle(matrix1) -> int:
    if not matrix1:
        return 0

    m = len(matrix1)  # m行
    n = len(matrix1[0])  # n列
    left = [0] * n  # initialize left as the leftmost boundary possible
    right = [n] * n  # initialize right as the rightmost boundary possible
    height = [0] * n

    maxarea = 0

    for i in range(m):

        cur_left, cur_right = 0, n  # 当前的最左最右的坐标
        # update height
        for j in range(n):  # 更新该行的每个位置的最大高度
            if matrix1[i][j] == 1:
                height[j] += 1
            else:
                height[j] = 0
        # update left
        for j in range(n):
            if matrix1[i][j] == 1:
                left[j] = max(left[j], cur_left)
            else:
                left[j] = 0
                cur_left = j + 1
        # update right
        for j in range(n - 1, -1, -1):
            if matrix1[i][j] == 1:
                right[j] = min(right[j], cur_right)
            else:
                right[j] = n
                cur_right = j
        # update the area
        for j in range(n):  # 对每行的每个位置的数都有计算
            maxarea = max(maxarea, height[j] * (right[j] - left[j]))

    return maxarea


waste = input()
matrix = []
while True:
    temp = input()
    if temp == ']':
        break
    else:
        line = [int(i) for i in re.findall("\d+", temp)]
        matrix.append(line)
print(maximalRectangle(matrix))
