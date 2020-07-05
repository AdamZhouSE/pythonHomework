n = int(input())
a = input().split(" ")
for i in range(0, n):
    a[i] = int(a[i])
a = sorted(a)
count = 0
i = 0
while i < n:
    waiting = 0
    for j in range(0, i):
        waiting += a[j]
    if waiting <= a[i]:
        count += 1
        i += 1
    else:
        a.remove(a[i])
        n -= 1
print(count)