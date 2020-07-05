n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
res = 0
if a[1] <= a[0]:
    res += a[0]
for i in range(1, n - 1):
    if a[i + 1] <= a[i]:
        res += a[i]
    if a[i - 1] < a[i]:
        res += a[i]
if a[n - 2] < a[n - 1]:
    res += a[n - 1]
print(res)