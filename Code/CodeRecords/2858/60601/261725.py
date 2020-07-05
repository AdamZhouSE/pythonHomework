n = eval(input())
if n == 1:
    print(1)
else:
    a = []
    for i in range(n):
        a.append([1]*n)
    for i in range(1,n):
        for j in range(1,n):
            a[i][j] = a[i-1][j] + a[i][j-1]
    print(a[-1][-1])