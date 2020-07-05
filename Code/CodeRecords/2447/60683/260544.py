m, n = [int(x) for x in input().split()]
ms = [int(x) for x in input().split()]
res = []
for i in range(n):
    left, right = [int(x) for x in input().split()]
    res.append(min(ms[left - 1:right]))
print(*res, end=' ')