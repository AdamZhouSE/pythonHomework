import sys

t=int(sys.stdin.readline())
for i in range(0,t):
    num,gap=map(int,sys.stdin.readline().split())
    sum=10*(num-1)
    sub=gap*(num-1)
    if sub>=sum:
        print(0)
    else:
        print(sum-sub)
