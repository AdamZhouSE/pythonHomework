import sys 
sys.setrecursionlimit(9000000)
t=int(input())
def f(a,b):
    result = 1
    for i in range(a-b):
        result*=a-i
        result//=i+1
    return result
for i in range(t):
    a,b=map(int,input().split())
    x=0
    if(a<b):x=f(a+b-2,a-1)
    else:x=f(a+b-2,b-1)
    print(x)