def divisorsSum(s):
    sumD = 0
    for i in range(1,s+1):
        if s % i == 0:
            sumD+=i
    return sumD
T = int(input())
for i in range(T):
    s = int(input())
    sum1 = divisorsSum(s)
    if sum1 < 2*s:
        print(1)
    else:
        print(0)