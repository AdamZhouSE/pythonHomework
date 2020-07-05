n = int(input())
a = input().split(" ")
b = input().split(" ")
for i in range(0, n):
    a[i] = int(a[i])
    b[i] = int(b[i])
a = sorted(a)
b = sorted(b)
total = 0
for i in range(0, n):
    total += a[i]
if (b[n-1] + b[n-2]) >= total:
    print("YES")
else:
    print("NO")