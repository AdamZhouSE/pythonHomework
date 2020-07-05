import sys

t=int(sys.stdin.readline())
for i in range(0,t):
    num=int(sys.stdin.readline())
    num1=0
    num2=0
    while num>0:
        if num%2==0:
            num2+=1
        else:
            num1+=1
        num=num//2
    print(num1^num2)