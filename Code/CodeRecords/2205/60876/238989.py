import sys

def times(n):
    if n%2==1:
        n=n-1
    if n==0:
        return 1
    elif n==2:
        return 1
    else:
        sum=0
        for i in range(0,n,2):
            sum+=times(i)*times(n-2-i)
        return sum
t=int(sys.stdin.readline())
for i in range(0,t):
    num=int(sys.stdin.readline())
    print(times(num))
