n = int(input()) + 1
a = [0] * n
for i in range(1, n):
    a[i] = int(input())
m = 1
for i in range(1, n):
    c = 1
    x = i
    while a[x] != -1:
        x = a[x]
        c += 1
    m = max(m, c)

print(m)
