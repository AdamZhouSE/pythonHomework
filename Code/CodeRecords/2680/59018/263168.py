import math

def paths(m,n):
    return math.factorial(n+m-2)/(math.factorial(n-1)*math.factorial(m-1))


T=int(input())
for i in range(T):
    m1,n1=input().split(' ')
    m=int(m1)
    n=int(n1)
    print(paths(m,n))