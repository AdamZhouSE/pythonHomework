T = int(input())
source = []
for x in range(0,T):
    source.append(int(input()))
for x in range(0,T):
    n = source[x]
    print(2*n*n*n+n)