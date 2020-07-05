m = int(input())
list1 = []
for i in range(m):
    t = input().split(",")
    t = [int(k) for k in t]
    list1.append(t)
n = len(list1[0])
threshold = int(input())
p = [[0] * (n + 1) for x in range(m + 1)]
for i in range(1, m + 1):
    for j in range(1, n + 1):
        p[i][j] = p[i - 1][j] + p[i][j - 1] - p[i - 1][j - 1] + list1[i - 1][j - 1]


def cal(x1, y1, x2, y2):
    return p[x2][y2] - p[x1 - 1][y2] - p[x2][y1 - 1] + p[x1 - 1][y1 - 1]


l, r, res = 1, min(m, n), 0
while l <= r:
    mid = (l + r) // 2
    flag = False
    for i in range(1, m - mid + 2):
        for j in range(1, n - mid + 2):
            temp = cal(i, j, i + mid - 1, j + mid - 1)
            if temp <= threshold:
                flag = True
                break
    if flag:
        res = mid
        l = mid + 1
    else:
        r = mid - 1
print(res)