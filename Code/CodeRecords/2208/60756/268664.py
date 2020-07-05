T=int(input())
for t in range(T):
    N=int(input())
    arr=list(map(int,input().split()))
    ans=["-1" for i in range(N)]
    for i in range(N):
        for j in range(i,-1,-1):
            if arr[i]>arr[j]:
                ans[i]=str(arr[j])
                break
    for i in range(N):
        print(ans[i]+' ',end="")
    print()
