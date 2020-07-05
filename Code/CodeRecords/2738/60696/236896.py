# 先对每一个点纵向寻找最大高度, 再横向寻找最大宽度, 求得最大面积(伪), 尽管不一定是当前点的最大面积, 但最大的矩形面积一定可以这样找到
def maximalRectangle(matrix): # m * n 矩阵
    m = len(matrix)
    n = len(matrix[0])
    max_height = [0 for i in range(0, n)]
    max_left = [0 for i in range(0, n)]
    min_right = [n-1 for i in range(0, n)]
    max_area = 0
    for i in range(0, m):
        left_border = 0
        right_border = n - 1
        for j in range(0, n):  # 更新最大高度和左边界
            if matrix[i][j] == 1:
                max_height[j] = max_height[j] + 1
                max_left[j] = max(max_left[j], left_border)
            else:
                max_height[j] = 0
                left_border = j + 1
                max_left[j] = 0
        # 更新右边界
        j = n-1
        while j >= 0:
            if matrix[i][j] == 1:
                min_right[j] = min(min_right[j], right_border)
            else:
                right_border = j - 1
                min_right[j] = n - 1
            j -= 1
            
        # 计算(伪)最大面积
        for j in range(0, n):
            if (min_right[j] - max_left[j] + 1) * max_height[j] > max_area:
                max_area = (min_right[j] - max_left[j] + 1) * max_height[j]
    return max_area


matrix = []
input()
while True:
    arr = input()
    if arr[-1] == ',':
        matrix.append([int(i) for i in arr.strip()[2:-3].split('","')])
    else:
        matrix.append([int(i) for i in arr.strip()[2:-2].split('","')])
        break
input()
print(maximalRectangle(matrix))