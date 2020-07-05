import sys

n=int(sys.stdin.readline())
for i in range(0,n):
    N=int(sys.stdin.readline())
    temp=N
    print(N,end=" ")
    N=N-5
    while(N>0):
        print(N,end=" ")
        N = N - 5
    while(N!=temp):
        print(N,end=" ")
        N=N+5
    print(N,end=" ")
    print()