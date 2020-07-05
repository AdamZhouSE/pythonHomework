n = int(input())
data = []
area = 0
for i in range(n):
    data.append(list(map(int, input().split(','))))
for r in range(n):
    for c in range(n):
        height = data[r][c]
        if height == 0:  # 这一格没有方块，直接跳过
            continue
        area += 2  # 先算上下底面积
        '''north'''
        if r == 0:
            area += height
        else:
            if height > data[r - 1][c]:
                area += height - data[r - 1][c]
        '''south'''
        if r == n - 1:
            area += height
        else:
            if height > data[r + 1][c]:
                area += height - data[r + 1][c]
        '''west'''
        if c == 0:
            area += height
        else:
            if height > data[r][c - 1]:
                area += height - data[r][c - 1]
        '''east'''
        if c == n - 1:
            area += height
        else:
            if height > data[r][c + 1]:
                area += height - data[r][c + 1]
print(area)
