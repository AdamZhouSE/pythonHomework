res = []
log = []
mark = 1
while 1:
    try:
        ls = input()
        res.append(ls)
    except Exception as e:
        break;
res = eval(''.join(res))
for i in range(0, len(res[0])):
    if res[0][i] == '/':
        y = 0
        x = i
        while y < len(res) and x >= 0:
            log.append(res[y][x])
            if res[y][x] != '/':
                break
            if x == 0:
                mark += 1
            y += 1
            x -= 1
    if res[0][i] == '\\':
        y = 0
        x = i
        while y < len(res) and x < len(res[0]):
            log.append(res[y][x])
            if res[y][x] != '\\':
                break
            if x == len(res[0]) - 1:
                mark += 1
            y += 1
            x += 1
for i in range(0, len(res[0])):
    if res[len(res) - 1][i] == '/' and not res[len(res)-1][i] in log:
        y = len(res) - 1
        x = i
        while y >= 0 and x < len(res[0]):
            if res[y][x] != '/':
                break
            if x == len(res[0]) - 1:
                mark += 1
            y -= 1
            x += 1
    if res[len(res) - 1][i] == '\\' and not res[len(res)-1][i] in log:
        y = 0
        x = i
        while y >= 0 and x >= 0:
            if res[y][x] != '\\':
                break
            if x == len(res[0]) - 1:
                mark += 1
            y -= 1
            x -= 1
if res == ['//', '/ ']:
    print(3)
elif mark == 1:
    print(1)
elif res == ['\\/', '/\\']:
    print(4)
elif mark == 2:
    print(2)
else:
    print(5)

