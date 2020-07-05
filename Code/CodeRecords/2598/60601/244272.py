line = input().split(' ')
M = int(line[0])
D = int(line[1])
data = []
findPath = []
ors = []
for i in range(M):
    line = input()
    order = []
    if ' ' in line:
        order = line.split(' ')
    else:
        order = [line[0],line[1:]]
    ors.append(order)
    # 插入操作
    if order[0] == 'A':
        n = int(order[1])
        if len(findPath)!=0:
            n = n + findPath[len(findPath)-1]
        data.append(divmod(n,D)[1])
    else:
        if len(order)==2:
            L = int(order[1])
        else:
            print(ors)
        num = data[len(data)-L:]
        num.sort()
        findPath.append(num[-1])
        print(num[-1])




