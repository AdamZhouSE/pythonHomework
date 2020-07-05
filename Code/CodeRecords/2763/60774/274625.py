import math

t = int(input())
for i in range(0,t):
    req = list(map(int,input().split(' ')))
    m = req[0]
    n = req[1]
    minArr = int(pow(2,n - 1))
    count = 0
    for kind in range(m - minArr + 1,0,-2):
        count = count + kind
    print(count)