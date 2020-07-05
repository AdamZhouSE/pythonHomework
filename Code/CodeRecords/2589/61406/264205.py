def lucas(n):
    if n==0:
        return 2
    elif n==1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)


T = int(input())
source = []
for x in range(0,T):
    source.append(int(input()))
for x in range(0,T):
    n = source[x]
    print(lucas(n)%1000000007)


