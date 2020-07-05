m = int(input())
list1 = []
for i in range(m):
    t = input().split(",")
    t = [int(k) for k in t]
    list1.append(t)
threshold = int(input())
p = [[0] * (len(list1[0]) + 1) for x in range(m + 1)]
for i in range(1, m + 1):
    for j in range(1, len(list1[0]) + 1):
        p[i][j] = p[i - 1][j] + p[i][j - 1] - p[i - 1][j - 1] + list1[i - 1][j - 1]
l, r, res = 0, min(m, len(list1[0])), 0
flag = False
while l <= r:
    mid = (l + r) // 2
    for i in range(m - mid + 1):
        for j in range(len(list1[0]) - mid + 1):
            if (p[i + mid][j + mid] - p[i][j + mid] - p[i + mid][j] + p[i][j]) <= threshold:
                flag = True
                break
    if flag:
        res = mid
        l = mid + 1
    else:
        r = mid - 1
print(res - 1)