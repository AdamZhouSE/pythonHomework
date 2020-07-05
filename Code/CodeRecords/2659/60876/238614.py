import sys

t=int(sys.stdin.readline())
for i in range(0,t):
    num1,num2=map(int,sys.stdin.readline().split())
    result=num2-num1-1
    print(result)