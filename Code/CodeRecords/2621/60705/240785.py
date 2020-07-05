a = list(map(int, input().split(",")))
m = a[0]
for i in range(0, len(a)-1):
    for j in range(i, len(a)):
        total = 0
        for k in range(i, j+1):
            total += a[k]
        if total > m:
            m = total
print(m)