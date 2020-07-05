from math import sqrt
from math import pow
def magicalBox(p:int,s:int):

    a=(p-sqrt(pow(p,2)-24*s))/12
    v=pow(a,3)-pow(a,2)*p/4+s*a/2
    return v


cases=int(input())
for _ in range(cases):
    ps=input().split()
    p,s=int(ps[0]),int(ps[1])
    print('%.5f' % magicalBox(p,s))