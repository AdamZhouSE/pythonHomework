

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
    res = []
    for i in range(0,test):
        line = list(map(int,input().split(' ')))
        a = line[0]
        b = line[1]
        i = 1
        while not isPrime(a + b + i):
            i += 1
        res.append(i)
    for i in range(0,test):
        print(res[i])

solve()