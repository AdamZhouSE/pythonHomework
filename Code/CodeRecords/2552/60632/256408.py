n, m = map(int, input().split(' '))
op = []
mine = ['0'] * n
result = []
for i in range(m):
    op.append(list(map(int, input().split(' '))))
mine_type = 1
for i in op:
    if i[0] == 1:
        left, right = i[1], i[2]
        for j in range(left - 1, right):
            mine[j] += str(mine_type)
        mine_type += 1
    else:
        left, right = i[1], i[2]
        tmp = max([len(x) for x in mine[left - 1:right]])
        result.append(tmp - 1)
for i in result:
    print(i)
