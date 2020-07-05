tests = int(input())
for i in range(0,tests):
    lent = int(input())
    ls = list(map(int,input().split()))
    res = 0
    for i in range(0,lent):
        short = ls[i]
        for j in range(i+1,lent):
            if short>ls[j]:
                short=ls[j]
            if res < short*(j-i+1):
                res = short*(j-i+1)
    print(res)