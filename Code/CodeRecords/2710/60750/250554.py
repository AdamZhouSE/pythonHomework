def solve():
    input1 = input().split(' ')
    n = int(input1[0])
    m = int(input1[1])

    information = []
    res = []
    for i in range(0,m):
        data = input().split(' ')
        if data[0] == 'M':
            information.append([int(data[1]),int(data[2])])
        else:
            information.sort()
            y = int(data[1])
            b = int(data[2])
            min_child = n + 1
            for j in range(0,len(information)):
                if information[j][0] <= y and b <= information[j][1] < min_child:
                    min_child = information[j][1]
                if information[j][0] > y:
                    break
            if min_child == n + 1:
                res.append(-1)
            else:
                res.append(min_child)

    for i in range(0,len(res)):
        print(res[i])


solve()
