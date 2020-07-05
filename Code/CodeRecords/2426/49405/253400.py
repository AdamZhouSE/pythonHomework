T = int(input())
for t in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[n - 1] == 0:
        print(0)
    elif a[n - 1] < 0:
        print(a[n - 1] * a[n - 2] * a[n - 3])
    else:
        print(max(a[n - 1] * a[n - 2] * a[n - 3], a[n - 1] * a[0] * a[1])) 