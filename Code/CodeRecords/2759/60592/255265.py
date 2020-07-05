import math
tests = int(input())
for i in range(0,tests):
    ls = list(map(int,input().split()))
    m,n,a,b = ls[0],ls[1],ls[2],ls[3]
    c = int(a*b/math.gcd(a,b))
    print(int(n/a)-int(m/a)+int(n/b)-int(m/b)-int(n/c)+int(m/c))