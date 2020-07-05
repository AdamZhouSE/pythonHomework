a = int(input())
b = int(input())
res = []
for i in range(0, max(a, b)):
    for j in range(0, max(a, b)):
        if (4*i + 2 * j == a) and i+j == b:
            res.append(i, j)

print(res)
