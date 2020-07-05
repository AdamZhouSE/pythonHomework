a = list(map(int, input().split(",")))
b = list(map(int, input().split(",")))
m = 0
for i in range(0, len(a)):
    for j in range(0, len(a)):
        cal = abs(a[i] - a[j]) + abs(b[i] - b[j]) + abs(i - j)
        if cal > m:
            m = cal
print(m)
