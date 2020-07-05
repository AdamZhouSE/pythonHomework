line = input().split(' ')
M = int(line[0])
D = int(line[1])
data = []
findPath = []
for i in range(M):
    order = input().split(' ')
    # 插入操作
    if order[0] == 'A':
        n = int(order[1])
        if len(findPath)!=0:
            n = n + findPath[len(findPath)-1]
        data.append(divmod(n,D)[1])
    else:
        L = int(order[1])
        num = data[len(data)-L:]
        num.sort()
        findPath.append(num[-1])
        print(num[-1])




