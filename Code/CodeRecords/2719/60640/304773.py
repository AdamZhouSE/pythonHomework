n = int(input())
operations = []
for i in range(n):
    operations.append(input())
# print(operations)
S = []
res = []
for op in operations:
    if op == 'B':
        print(len(S))
        res.append(len(S))
    else:
        op1 = op.split(" ")
        cnt = 0
        del_ele = []
        for m in S:
            if m[0] <= int(op1[1]) <= m[1] or m[0] <= int(op1[2]) <= m[1] or int(op1[1]) <= m[0] < m[1] <= int(op1[2]):
                cnt += 1
                del_ele.append(m)
        for i in range(cnt):
            S.remove(del_ele[i])
        S.append([int(op1[1]), int(op1[2])])
        print(cnt)
        res.append(cnt)
# if res == [0, 1, 1, 0, 0, 2, 0, 3, 0, 0]:
#    print(operations)

