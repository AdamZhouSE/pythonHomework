

def solve():
    test = int(input())
    res = []
    for i in range(0,test):
        n = int(input())
        j = 0
        tmp= []
        while n - j * 5 > 0:
            tmp.append(n - j * 5)
            j += 1
        reverse_tmp = sorted(tmp)
        tmp.append(n - j * 5)
        tmp = tmp + reverse_tmp
        res.append(tmp)

    for i in range(0,test):
        for j in range(0,len(res[i])):
            print(res[i][j],end=' ')
        print()

solve()