T=int(input())
for i in range(0,T):
    N,K=map(int,input().split())
    a=list(map(int,input().split()))
    Max=0
    for j in range(0,N-K+1):
        Max=max(Max,sum(a[j:j+K]))
    print(Max)        