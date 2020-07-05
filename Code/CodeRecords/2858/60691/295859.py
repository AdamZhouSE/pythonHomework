n = int(input())

l = [[]for i in range(n)]

for i in range(n):
    for j in range(n):
        l[i].append(0)

for i in range(n):
    l[0][i] = 1
    l[i][0] = 1

for i in range(1, n):
    for j in range(i, n):
        l[i][j] = l[i-1][j] + l[i][j-1]
        l[j][i] = l[j-1][i] + l[j][i-1]

print(l[n-1][n-1])