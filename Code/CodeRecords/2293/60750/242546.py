def solve():
    test = int(input())
    res = []
    for i in range(0,test):
        num = int(input())
        data = list(map(int,input().split(' ')))
        k = int(input())
        data.sort()
        res.append(data[k - 1])
    for i in range(0,test):
        print(res[i])


solve()