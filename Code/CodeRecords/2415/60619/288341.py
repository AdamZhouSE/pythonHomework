def find_path(l, r):
    if l < r:
        path.append(root[l][r] + 1)
        find_path(l, root[l][r] - 1)
        find_path(root[l][r] + 1, r)
    elif l == r:
        if l+1 not in path:
            path.append(l + 1)
    elif l > r:
        if l+1 not in path:
            path.append(l + 1)


length = int(input())
nums = [int(i) for i in input().strip().split(" ")]
area = []
root = []
# 初始化
for i in range(length):
    a = []
    r = []
    for j in range(length):
        a.append(-1)
        r.append(-1)
    area.append(a)
    root.append(r)
for i in range(length):
    area[i][i] = nums[i]
    root[i][i] = i

le = 1
while le < length:
    for i in range(length - le):
        j = i + le
        area[i][j] = area[i + 1][j] + area[i][i]
        root[i][j] = i
        for k in range(i + 1, j):
            if area[i][j] < area[i][k - 1] * area[k + 1][j] + nums[k]:
                area[i][j] = area[i][k - 1] * area[k + 1][j] + nums[k]
                root[i][j] = k
    le += 1
print(area[0][length - 1])
path = []
find_path(0, length - 1)

print(*path, end=" ")
