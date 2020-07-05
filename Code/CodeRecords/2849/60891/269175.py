n = int(input())
a = [int(i) for i in input().split()]
a.sort()
is_found = True
for i in range(1, n):
    if a[i] % a[0] != 0:
        is_found = False
        break

if is_found:
    print(a[0])
else:
    print(-1)
