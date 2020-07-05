def searchMatrix(matrix, target):
    m = len(matrix)
    if m == 0:
        return False
    n = len(matrix[0])

    # 二分查找
    left, right = 0, m * n - 1
    while left <= right: #把二维数组看成一维的，index = i*n+j
        pivot_idx = (left + right) // 2 # 基准
        pivot_element = matrix[pivot_idx // n][pivot_idx % n]
        if target == pivot_element:
            return True
        else:
            if target < pivot_element:
                right = pivot_idx - 1
            else:
                left = pivot_idx + 1
    return False

n = int(input())
matrix = []
for i in range(n):
    line = [int(i) for i in input().split(",")]
    matrix.append(line)
target = int(input())
print(searchMatrix(matrix,target))