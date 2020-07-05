import math
t=int(input())
for i in range(t):
    p,s=map(int,input().split())
    temp=(p-math.sqrt(p*p-24*s))/12
    h=(p/4-2*temp)
    print('%.5f'%(temp**2*h))