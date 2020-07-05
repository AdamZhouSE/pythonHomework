t=int(input())
for k in range(0,t):
    n,money=map(int,input().split())
    if n%2==0:
        n=n//2
    else :
        n=(n//2)+1
    print(n*money)