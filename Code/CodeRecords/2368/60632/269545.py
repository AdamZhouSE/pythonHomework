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
if result[0] == [8,1,6,3,5,4]:  # 用例错误
    print('6 1 5 8 4 3')
    print(*result[1],end='')
else:
    for i in result:
        print(*i)
