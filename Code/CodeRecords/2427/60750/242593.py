def solve():
    test = int(input())
    res  = []
    for i in range(0,test):
        num = int(input())
        data = list(map(int,input().split(' ')))
        tmp = []
        tmp_index = []
        index = []
        for j in range(0,num):
            if data[j] not in tmp:
                tmp.append(data[j])
            else:
                index.append(data.index(data[j]) + 1)
        index.sort()
        if len(index) == 0:
            res.append(-1)
        else:
            res.append(index[0])
    for i in range(0,test):
        print(res[i])

solve()

