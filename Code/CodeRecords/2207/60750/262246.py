

def solve():
    test = int(input())
    res = []
    for i in range(0,test):
        line1 = list(map(int,input().split(' ')))
        a = line1[0]
        b = line1[1]
        s = (b + 1) * b // 2
        if a > s:
            res.append(1)
        else:
            res.append(0)
    for i in range(0,test):
        print(res[i])

solve()