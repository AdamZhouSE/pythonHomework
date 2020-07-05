import sys

n=int(sys.stdin.readline())
prime=[2,3,5,7,11,13,17,19,23,29,31]
for i in range(0,n):
    num=0
    m,t=map(int,sys.stdin.readline().split())
    for j in range(m,t+1):
        sum=0
        while j!=0:
            sum+=j%2
            j=j//2
        if sum in prime:
            num+=1
    print(num)