def count(matrix, num):
    i, j = len(matrix)-1, 0
    cnt = 0
    while i >= 0 and j < len(matrix[0]):
        if matrix[i][j] <= num:
            cnt += i+1
            j += 1
        else:
            i -= 1
    return cnt


size = int(input())
matrix = []
for _ in range(size):
    matrix.append(list(map(int, input().split(','))))
k = int(input())
lo, hi = matrix[0][0], matrix[-1][-1]
while lo < hi:
    mid = (lo + hi) // 2
    cnt = count(matrix, mid)
    if cnt < k:
        lo = mid + 1
    else:
        hi = mid
print(lo)

