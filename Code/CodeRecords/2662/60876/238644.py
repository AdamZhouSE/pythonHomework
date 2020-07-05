import sys

t=int(sys.stdin.readline())
for i in range(0,t):
    num=int(sys.stdin.readline())
    sum=0
    while num>0:
        if num%2==1:
            sum+=1
        num=num//2
    if sum%2==0:
        print("even")
    else:
        print("odd")