import sys

n=int(sys.stdin.readline())
for i in range(0,n):
    N,K=map(int,sys.stdin.readline().split())
    list=sys.stdin.readline().split()
    max=0
    for i in range(0,N-K+1):
        sum=0
        for j in range(i,i+K):
            sum+=int(list[j])
        if sum>max:
            max=sum
    print(max)