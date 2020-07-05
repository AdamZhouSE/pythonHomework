
import math

def isPrime(a):
    b = int(math.sqrt(a))
    if a < 2:
        return False
    for i in range(2,b + 1):
        if a % i == 0:
            return False

    return True

def solve():
    test = int(input())
    res= []
    for i in range(0,test):
        line = input().split(' ')
        m = int(line[0])
        n = int(line[1])
        tmp = []
        for i in range(m,n + 1):
            if isPrime(i):
                tmp.append(i)

        res.append(tmp)

    for i in range(0,test):
        if len(res[i]) != 0:
            for j in range(0, len(res[i]) - 1):
                print(res[i][j], end=' ')
            print(res[i][len(res[i]) - 1])

solve()