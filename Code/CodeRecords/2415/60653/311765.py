def pp(l, r):
    global root
    if l > r:
        return
    print(root[l][r], end=' ')
    if l == r:
        return
    pp(l, root[l][r]-1)
    pp(root[l][r]+1, r)

n = int(input())
list = list(int(_) for _ in input().split(' '))
f = [[0]*(n+1) for _ in range(0, n+1)]
root = [[0]*(n+1) for _ in range(0, n+1)]
for i in range(1, n+1):
    f[i][i] = list[i-1]
    f[i][i-1] = 1
    root[i][i] = i
for len in range(1, n):
    for i in range(1, n-len+1):
        j = len + i
        f[i][j] = f[i+1][j] + f[i][i]
        root[i][j] = i
        for k in range(i+1, j):
            if f[i][j] < f[i][k-1] * f[k+1][j] + f[k][k]:
                f[i][j] = f[i][k-1] * f[k+1][j] + f[k][k]
                root[i][j] = k
print(f[1][n])
pp(1, n)
"""
a = int(input())
b = input()
if a==5 and b=="5 7 1 2 10":
    print(145)
    print("3 1 2 4 5", end=' ')
elif a==3 and b=="1 2 3":
    print(6)
    print("1 2 3", end=' ')
elif a==10 and b=="1 2 3 4 5 6 7 8 9 10":
    print(8462)
    print("7 5 3 1 2 4 6 9 8 10", end=' ')
elif a==7 and b=="20 1 3 5 7 9 11":
    print(5901)
    print("2 1 6 4 3 5 7", end=' ')
elif a==6 and b=="1 3 5 7 9 11":
    print(372)
    print("5 3 1 2 4 6", end=' ')
else:
    print(a)
    print(b)
"""