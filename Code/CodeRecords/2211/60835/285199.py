x = input().split()
queens = []
for t in range(int(x[0])):
    tem = input().split()
    if tem[1] == '0':
        queens.append(tem[0])
    else:
        queens.append(tem[0] + queens[int(tem[1]) - 1])
res = []
for h in range(int(x[1])):
    tem = input()
    cnt = 0
    for x in queens:
        if x[0:len(tem)] == tem:
            cnt = cnt + 1
    res.append(cnt)
for x in res:
    print(x)