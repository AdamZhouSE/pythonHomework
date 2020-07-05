

def solve():
    test = int(input())
    res = []
    for i in range(0,test):
        n = int(input())
        fn = 0
        start = 1
        for i in range(0,n):
            tmp = 1
            for j in range(0,i + 1):
                tmp *= (start + j)
                if j == i:
                    start = start + j + 1
            fn += tmp
        res.append(fn)
    for i in range(0,len(res)):
        print(res[i])

solve()