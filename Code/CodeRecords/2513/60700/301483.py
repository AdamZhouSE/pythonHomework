n = int(input())
matrix = []
for i in range(n):
    row = list(map(int, input().split(',')))
    matrix.append(row)
k = int(input())
l = matrix[0][0]
r = matrix[n - 1][n - 1]
mid = -1
while l < r:
    mid = (l + r) // 2
    x = 0
    y = n - 1
    c = 0
    while x < n:
        if matrix[x][y] > mid:
            y -= 1
            if y < 0:
                break
        else:
            x += 1
            c += y + 1
    if c >= k:
        r = mid
    else:
        l = mid + 1
print(l)
