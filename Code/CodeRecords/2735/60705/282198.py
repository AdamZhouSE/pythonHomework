[n, m] = list(map(int, input().split(" ")))
try:
    a = list(map(int, input().split(" ")))
except ValueError:
    a = input()
    print(a)
for i in range(0, m):
    [l, r, k] = list(map(int, input().split(" ")))
    tem = a[l - 1:r]
    tem.sort()
    print(tem[k - 1])

