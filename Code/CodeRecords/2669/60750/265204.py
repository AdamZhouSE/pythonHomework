

def solve():
    test = int(input())
    res = []
    for i in range(0,test):
        num = int(input())
        tmp = []
        for j in range(num,-1,-1):
            if j & num == j:
                tmp.append(j)
        res.append(tmp)

    for i in range(0,test):
        for j in range(0,len(res[i])):
            print(res[i][j],end = ' ')
        print()

solve()
