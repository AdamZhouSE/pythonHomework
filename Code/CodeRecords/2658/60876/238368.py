import sys

t=int(sys.stdin.readline())
for i in range(0,t):
    num1,num2=map(int,sys.stdin.readline().split())
    num=sys.stdin.readline().split()
    result=0
    for item in num:
        if int(item)%num2==0:
            result=result|int(item)
    print(result)