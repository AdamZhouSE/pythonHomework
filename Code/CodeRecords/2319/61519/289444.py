n=int(input())
num=[]*n
for i in range(n):
    tem=list(input().split(","))
    for j in range(len(tem)):
        tem[j]=int(tem[j])
    num.append(tem)
count, total= 0,0
directions = [(0, 1), (1, 0)]
for i in range(n):
    for j in range(n):
        total += num[i][j]
        if num[i][j] > 1: count += num[i][j] - 1
        for dx, dy in directions:
            x, y = i + dx, j + dy
            if x < n and y < n:
                count += min(num[i][j], num[x][y])
res=6 * total - 2 * count
print(res)