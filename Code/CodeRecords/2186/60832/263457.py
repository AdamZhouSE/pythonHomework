All = int(input())

for q in range(0, All):
    n=int(input())
    ans=0

    for i in range(1,n+1):
        ans+=(n-i+1)*i
    print(ans)