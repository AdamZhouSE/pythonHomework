import sys

t=int(sys.stdin.readline())
for i in range(0,t):
    num1,num2=map(int,sys.stdin.readline().split())
    index=1
    while num1%2==num2%2:
        index+=1
        num1=num1//2
        num2=num2//2
    print(index)
