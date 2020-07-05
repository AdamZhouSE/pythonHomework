def searchMatrix(matrix, target):
    if not matrix:
        return False
    row = len(matrix)
    col = len(matrix[0])
    left = 0
    right = row * col - 1
    while left <= right:
        mid = left + (right - left) // 2
        num = matrix[mid // col][mid % col]
        if num == target:
            return True
        elif num < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


rowNum = int(input())
inputMatrix = []
for index in range(rowNum):
    s = input().split(",")
    rowList = []
    for item in s:
        rowList.append(int(item))
    inputMatrix.append(rowList)
inputTarget = int(input())
print(searchMatrix(inputMatrix, inputTarget))