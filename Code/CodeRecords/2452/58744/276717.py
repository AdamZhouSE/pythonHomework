n = int(input())

matrix = []
for i in range(n):
    matrix.append(list(eval(input())))

target = int(input())


def searchMatrix(matrix, n, target):
    m = len(matrix)
    if m == 0:
        return False

    # Binary Search
    left, right = 0, m * n - 1
    while left <= right:
        pivot = (left + right) // 2
        # row = pivot // n, col = pivot % n
        pivot_num = matrix[pivot // n][pivot % n]
        if target == pivot_num:
            return True
        else:
            if target < pivot_num:
                right = pivot - 1
            else:
                left = pivot + 1
    return False


print(searchMatrix(matrix, n, target))
