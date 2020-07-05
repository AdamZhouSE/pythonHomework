a = int(input())
b = int(input())
res = []
for i in range(0, max(a, b)+1):
    for j in range(0, max(a, b)+1):
        if (4*i + 2 * j == a) and i+j == b:
            res.append(i)
            res.append(j)

print(res)

