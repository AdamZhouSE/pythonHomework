n = int(input())
a = []
for i in range(n):
    a.append([int(j) for j in input().split()])
res = 0
for i in a:
    r = i[0] + i[1]
    res = max(res, r)
print(res)