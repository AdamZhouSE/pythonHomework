import sys

t=int(sys.stdin.readline())
for i in range(0,t):
    num1,num2=map(int,sys.stdin.readline().split())
    max=0
    for j in range(0,num2):
        max+=2**j
    print(max-num1+1)