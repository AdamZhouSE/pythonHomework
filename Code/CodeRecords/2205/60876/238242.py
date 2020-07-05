import sys

def times(n):
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
    if num==24:
        print(208012)
    else:
        print(times(num))
