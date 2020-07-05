import sys

def times(n):
    if n==0:
        return 1
    elif n==2:
        return 1
    elif n==4:
        return 2
    elif n==6:
        return 5
    elif n==8:
        return 14
    elif n==10:
        return 42
    elif n==12:
        return 132
    elif n==14:
        return 429
    elif n==16:
        return 1430
    elif n==18:
        return 4862
    elif n==20:
        return 16796
    elif n==22:
        return 58786
    elif n==24:
        return 208012
    else:
        sum=0
        for i in range(0,n,2):
            sum+=times(i)*times(n-2-i)
        return sum
t=int(sys.stdin.readline())
for i in range(0,t):
    num=int(sys.stdin.readline())
    print(times(num))
