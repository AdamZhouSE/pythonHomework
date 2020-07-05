n = int(input())
a = [int(i) for i in input().split()]
a.sort()
res = -1
is_found = False
for i in range(0, n - 1):
    for j in range(i + 1, n):
        if a[j] % a[i] == 0:
            res = a[i]
            is_found = True
            break
    if is_found:
        break
print(res)