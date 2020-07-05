n = eval(input())
row = [False] * n
col = [False] * n
days = []
for d in range(n ** 2):
    x, y = list(map(int, input().split(' ')))
    if not row[x - 1] and not col[y - 1]:
        days.append(d + 1)
        row[x - 1] = True
        col[y - 1] = True
print(*days)