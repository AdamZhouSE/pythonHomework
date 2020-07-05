import sys

t=int(sys.stdin.readline())
def times(n,m):
    sum=0
    while m>1:
        if n%m==0:
            sum+=1
            n-=1
        else:
            m-=1
    return sum
for i in range(0,t):
    x,y,z=map(int,sys.stdin.readline().split())
    print(times(x,z),end=" ")
    print(times(y,z))