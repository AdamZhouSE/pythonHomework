T = int(input())
source = []
for x in range(0,T):
    source.append(int(input()))
for x in range(0,T):
    n = source[x]
    divisorsSum = 0
    for a in range(1,n+1):
        if n%a==0:
            divisorsSum = divisorsSum + a
    if divisorsSum<2*n:
        print(1)
    else:
        print(0)