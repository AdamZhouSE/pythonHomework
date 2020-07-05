

def solve():
    test = int(input())
    res = []
    for i in range(0,test):
        line1 = input().split(' ')
        n = int(line1[0])
        x = int(line1[1])
        res.append((10 - x) * (n - 1))

    for i in range(0,test):
        print(res[i])

solve()
