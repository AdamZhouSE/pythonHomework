import sys 
sys.setrecursionlimit(9000000)
t=int(input())
def f0(n):
    if(n==1):
        return 1
    else:
        return n*f0(n-1)
def f(a,b):
    if(a==b):
        return 1
    else:
        return f0(a)//(f0(b)*f0(a-b))
for i in range(t):
    a,b=map(int,input().split())
    x=0
    if(a<b):x=f(a+b-2,a-1)
    else:x=f(a+b-2,b-1)
    print(x)