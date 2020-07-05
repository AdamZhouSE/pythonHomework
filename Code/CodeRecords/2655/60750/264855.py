

def solve():
    test = int(input())
    res = []
    for i in range(0,test):
        n = int(input())
        j = 0
        while True:
            tmp = n + j
            while tmp % 2 == 0:
                tmp = tmp // 2
            if tmp == 1:
                res.append(n + j)
                break
            else:
                j += 1
    for i in range(0,test):
        print(res[i])

solve()