n = int(input())
matrix = []

for i in range(n):
    li = list(eval(input()))
    matrix.append(li)
    
target = int(input())

row = len(matrix)
col = len(matrix[0])
left = 0
right = row * col
while left < right:
    mid = left + (right - left) // 2
    if matrix[mid // col][mid % col] < target:
        left = mid + 1
    else:
        right = mid

print(left < row * col and matrix[left // col][left % col] == target)
 