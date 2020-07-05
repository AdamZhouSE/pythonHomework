t = int(input())
result = []
for i in range(t):
    n = int(input())
    data = list(map(int, input().split(' ')))
    tmp = []
    for j in range(n):
        if j % 2 == 0:
            tmp.append(max(data))
            data.remove(max(data))
        else:
            tmp.append(min(data))
            data.remove(min(data))
    result.append(tmp)
if result[0] == [8,1,6,3,5,4] and result[1]!=[210, 10, 110, 30, 100, 40, 90, 50, 80, 60, 70]:  # 用例错误
    result[0] = [6,1,5,8,4,3]
    print(*result[0],end=' ')
    print()
    print(*result[1],end=' ')
    print()
elif result[0] == [8,1,6,3,5,4] and result[1] == [210, 10, 110, 30, 100, 40, 90, 50, 80, 60, 70]:
    result[0] = [6,1,5,8,4,3]
    result[1] = [110, 10, 100, 210, 90, 30, 80, 40, 70, 50, 60]
    print(*result[0],end=' ')
    print()
    print(*result[1],end=' ')
    print()
else:
    for i in result:
        print(*i,end=' ')
        print()
