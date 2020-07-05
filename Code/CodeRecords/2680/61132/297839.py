import functools
def jiecheng(n):
    if n==0:return 1
    return functools.reduce(lambda x,y:x*y,range(1,n+1))
n = int(input())
for j in range(n):
    n,m=map(int,input().split())
    print(jiecheng(n+m-2)//jiecheng(m-1)//jiecheng(n-1))