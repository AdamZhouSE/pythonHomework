T = int(input())
source = []
for x in range(0,T):
    source.append(int(input()))
for x in range(0,T):
    n = source[x]
    sum = 0
    for a in range(1,n+1):
        for b in range(1,a+1):
            sum = sum + b
    print(sum)