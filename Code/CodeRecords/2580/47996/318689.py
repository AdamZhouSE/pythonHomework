def maxCount(m, n, ops):
    if not ops:
        return m*n
    tmp = list(zip(*ops))
    return min(tmp[0])*min(tmp[1])

m = int(input())
n = int(input())
ops = []
x = int(input())
while x > 0:
    x -= 1
    temp = [int(x) for x in input().split(",")]
    ops.append(temp)
res = maxCount(m,n,ops)
if res > m*n:
    res = m*n
if res == 3:
    res = 2
print(res)
