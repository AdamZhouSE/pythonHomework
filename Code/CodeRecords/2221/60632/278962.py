n, m = map(int, input().split(' '))
link = []
for i in range(m):
    link.append(list(map(int, input().split(' '))))
adj = [[0 for i in range(n)] for j in range(n)]
for i in link:
    adj[i[0] - 1][i[1] - 1] = 1
for times in range(2):
    for i in range(n):
        for j in range(n):
            if adj[i][j] == 1:
                for k in range(n):
                    if adj[j][k] == 1 and i != k:
                        adj[i][k] = 1
count = 0
for i in range(n):
    tmp = []
    for j in range(n):
        if j != i:
            tmp.append(adj[j][i])
    if all(tmp):
        count += 1
print(count)
