n = int(input())
data = [[]]
for _ in range(0, n):
    [v, opt, x] = list(map(int, input().split(" ")))
    temp = data[v].copy()
    # 插入x
    if opt == 1:
        temp.append(x)
    # 删除x
    elif opt == 2:
        if x in temp:
            for i in range(0, len(temp)):
                if temp[i] == x:
                    temp.pop(i)
                    break
    # 查询x的排名
    elif opt == 3:
        count = 0
        for num in temp:
            if num < x:
                count += 1
        print(count+1)
    # 查询排名为x的数
    elif opt == 4:
        temp.sort()
        print(temp[x-1])
    # 求x的前驱
    elif opt == 5:
        t = []
        for num in temp:
            if num < x:
                t.append(num)
        if len(t) == 0:
            print(- 2**31 + 1)
        else:
            print(max(t))
    # 求 x 的后继
    else:
        t = []
        for num in temp:
            if num > x:
                t.append(num)
        if len(t) == 0:
            print(2**31)
        else:
            print(min(t))
    data.append(temp)


