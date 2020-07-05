n = int(input())
x = [0 for i in range(n)]
y = [0 for i in range(n)]
ans = 0
res = [0 for i in range(n)]


def dfs(i):
    res[i] = 1
    for j in range(n):
        if res[j] != 1 and (x[i] == x[j] or y[i] == y[j]):
            dfs(j)


for i in range(n):
    tmp = input()
    tmp = tmp.split(" ")
    x[i] = int(tmp[0])
    y[i] = int(tmp[1])
for i in range(n):
    if res[i] != 1:
        dfs(i)
        ans += 1
print(ans - 1)
