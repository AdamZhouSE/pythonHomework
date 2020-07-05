import sys
import math

n=int(sys.stdin.readline())
for i in range(0,n):
    num1,num2=map(int,sys.stdin.readline().split())
    num3=1
    now=num1+num2+num3
    while True:
        prime=True
        for j in range(2,int(math.sqrt(now))+1):
            if now%j==0:
                now=now+1
                num3=num3+1
                prime=False
                break
        if prime==True:
            break
    print(num3)