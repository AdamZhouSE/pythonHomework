m = int(input())
mat = []
for i in range(m):
    t = input().split(",")
    t = [int(k) for k in t]
    mat.append(t)
threshold = int(input())
m, n = len(mat), len(mat[0])
P = [[0] * (n + 1) for _ in range(m + 1)]
for i in range(1, m + 1):
    for j in range(1, n + 1):
        P[i][j] = P[i - 1][j] + P[i][j - 1] - P[i - 1][j - 1] + mat[i - 1][j - 1]
        
        
def getRect(x1, y1, x2, y2):
    return P[x2][y2] - P[x1 - 1][y2] - P[x2][y1 - 1] + P[x1 - 1][y1 - 1]
        
    
l, r, ans = 1, min(m, n), 0
while l <= r:
    mid = (l + r) // 2
    find = any(getRect(i, j, i + mid - 1, j + mid - 1) <= threshold for i in range(1, m - mid + 2) for j in range(1, n - mid + 2))
    if find:
        ans = mid
        l = mid + 1
    else:
        r = mid - 1
print(ans)

'''
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
'''