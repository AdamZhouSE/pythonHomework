import sys

t=int(sys.stdin.readline())
def min(num):
    sum=0
    for j in range(0,num+1):
        sum+=j
    return sum
for i in range(0,t):
    m,n=map(int,sys.stdin.readline().split())
    if m<min(n):
        print(0)
    else:
        print(1)