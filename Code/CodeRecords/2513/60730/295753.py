def count(target, l):
    i = 0
    j = l - 1
    counter = 0
    while j >= 0 and i < l:
        if matrix[i][j] <= target:  # !!! 小于等于，必须包含相等，即便等于目标值的数量
            counter += j + 1
            i += 1
        else:
            j -= 1
    return counter


num = int(input())
matrix = []
for i in range(num):
    matrix.append(list(map(int, input().split(","))))
k = int(input())
lo = matrix[0][0]
n = len(matrix)
hi = matrix[n - 1][n - 1]
while lo < hi:
    mid = lo + ((hi-lo) >> 1)
    c = count(mid, n)
    if c < k:
        lo = mid + 1
    else:
        hi = mid
print(hi)
