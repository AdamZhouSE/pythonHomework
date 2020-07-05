def solve():
    test = int(input())
    res = []
    for i in range(0, test):
        num = int(input())
        data = list(map(int, input().split(' ')))
        max_num = 0
        for j in range(0,num):
            for k in range(j + 1,num):
                if data[k] - data[j] > max_num:
                    max_num = data[k] - data[j]
        res.append(max_num)
    for i in range(0,test):
        print(res[i])


solve()