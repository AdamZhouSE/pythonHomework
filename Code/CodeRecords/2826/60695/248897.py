n = int(input())
a = input().split(" ")
for i in range(0, n):
    a[i] = int(a[i])
a = sorted(a)
count = 0
for i in range(1, n):
    if a[i] == a[i-1]:
        a[i] += 1
        count += 1
    elif a[i] < a[i-1]:
        count += (a[i-1] - a[i] + 1)
        a[i] = a[i-1] + 1
print(count)