import math
def check(x):
    if x<=1:
        return False
    if x==2 or x==3:
        return True
    if x%2==0 or x%3==0:
        return False
    for i in range(2,int(math.sqrt(x))):
        if x%i==0:
            return False
    return True
def prim(m,n):
    cnt = 0
    for i in range(m,n+1):
        b = bin(i)
        b  = b[2:]
        x = b.count('1')
        if check(x):
            cnt = cnt+1
    return cnt
        
for i in range(int(input())):
    mn = list(map(int,input().split()))
    m = int(mn[0])
    n = int(mn[1])
    print(prim(m,n))