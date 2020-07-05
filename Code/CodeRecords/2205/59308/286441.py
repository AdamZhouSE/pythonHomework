from math import factorial as fac
T = int(input())
def cat(n):
    return fac(2*n)//fac(n+1)//fac(n)
for _ in range(T):
    a = int(input())
    print(cat(a//2))


