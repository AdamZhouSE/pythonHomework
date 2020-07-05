[n, m] = list(map(int, input().split(" ")))
a = list(map(int, input().split(" ")))
for i in range(0, m):
    [l, r, k] = list(map(int, input().split(" ")))
    tem = a[l - 1:r]
    tem.sort()
    print(tem[k - 1])

