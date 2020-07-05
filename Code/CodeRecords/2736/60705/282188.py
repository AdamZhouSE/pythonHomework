[n, m] = list(map(int, input().split(" ")))
a = list(map(int, input().split(" ")))
for i in range(0, m):
    op = input().split(" ")
    if op[0] == "Q":
        [l, r, k] = list(map(int, op[1:]))
        tem = a[l-1:r]
        tem = tem.sort()
        print(tem[k-1])
    else:
        [x, y] = list(map(int, op[1:]))
        a[x-1] = y
