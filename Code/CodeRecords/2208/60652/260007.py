T=int(input())
for sample in range(T):
    n=int(input())
    a=list(map(int,input().split()))
    print(-1,end=' ')
    for i in range(1,n):
        index=i
        ans=-1
        while index>0:
            index-=1
            if a[i]>a[index]:
                ans=a[index]
                break
        print(ans,end=' ')
    print()           