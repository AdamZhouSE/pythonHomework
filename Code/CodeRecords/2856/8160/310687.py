n = int(input())
x = [0 for j in range(n + 5)]
h = [0 for j in range(n + 5)]
f = [[0, 0, 0] for j in range(n + 5)]
x[0] = -2000000000
for i in range(n):
    tmp = input()
    tmp = tmp.split(" ")
    j = i + 1
    x[j] = int(tmp[0])
    h[j] = int(tmp[1])
    f[j][0] = max(f[j - 1][0], f[j - 1][1])
    if x[j - 1] + h[j - 1] < x[j]:
        f[j][0] = max(f[j][0], f[j - 1][2])
    if x[j - 1] < x[j] - h[j]:
        f[j][1] = max(f[j - 1][0], f[j - 1][1]) + 1
    if x[j - 1] + h[j - 1] < x[j] - h[j]:
        f[j][1] = max(f[j][1], f[j - 1][2] + 1)
    f[j][2] = max(f[j - 1][0], f[j - 1][1]) + 1
    if x[j - 1] + h[j - 1] < x[j]:
        f[j][2] = max(f[j][2], f[j - 1][2] + 1)
print(max(f[n][0], f[n][1], f[n][2]))
