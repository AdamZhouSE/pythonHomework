def solve():
    num = int(input())
    data = list(map(int,input().split(' ')))
    minus = 0
    equal = False
    res = 0
    for i in range(0,num):
        res += min(abs(data[i] - 1),abs(data[i] + 1))
        if abs(data[i] - 1)> abs(data[i] + 1):
            minus += 1
        elif abs(data[i] - 1) == abs(data[i] + 1):
            equal = True
    if minus % 2 == 1:
        if not equal:
            res += 2
    print(res)

solve()