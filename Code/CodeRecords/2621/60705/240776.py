a = list(map(int, input().split(",")))
m = a[0]
for i in range(0, len(a)-1):
    for j in range(i+1, len(a)):
        total = 0
        for k in range(i, j):
            total += a[k]
        if total > m:
            m = total
print(m)