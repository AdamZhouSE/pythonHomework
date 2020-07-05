T=int(input())
for t in range(T):
    a,b=map(int,input().split())
    n=int(input())
    d=b-a
    print(a+(n-1)*d)