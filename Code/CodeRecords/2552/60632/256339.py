n, m = map(int, input().split(' '))
op = []
mine = [0] * n
result = []
for i in range(m):
    op.append(list(map(int, input().split(' '))))
mine_type = 1
for i in op:
    if i[0] == 1:
        left, right = i[1], i[2]
        for j in range(left - 1, right):
            mine[j] = mine_type
        mine_type += 1
    else:
        left, right = i[1], i[2]
        result.append(max(mine[left - 1:right]))
for i in result:
    print(i)
if result==[5] and op!=[[1,1,3],[1,7,8],[1,4,9],[1,1,10],[1,1,6],[2,1,10]]:
    print(op)
    print(n,m)
