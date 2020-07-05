T=int(input())
for tt in range(T):
    n=int(input())
    a=list(map(int,input().split()))
    k=int(input())
    ans=1
    for i in a:
        ans*=i
    print(ans%k)