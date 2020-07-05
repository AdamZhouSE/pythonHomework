All = int(input())

for q in range(0, All):
    n=int(input())

    ar=list(map(int,input().split()))
    ans=max(ar)

    for i in range(n-1):
        for j in range(i+1,n):
            temp=min(ar[i:j])
            if temp*(j-i)>ans:
                ans=temp*(j-i)
    print(ans)