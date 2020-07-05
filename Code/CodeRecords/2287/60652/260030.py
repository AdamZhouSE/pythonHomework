T=int(input())
for sample in range(T):
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(0,n-1):
        index=i+1
        ans=-1
        while index<n:
            if a[index]>=a[i]:
                ans=a[index]
                break
            index+=1                
        print(ans,end=' ')
    print(-1)        