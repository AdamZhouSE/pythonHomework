def exam23():
    T = int(input())
    for t in range(T):
        k=int(input())
        n=int(input())
        x = input().split(" ")
        a = []
        for item in x:
            a.append(int(item))
        pre=a[0]
        ans=0
        for i in range(1,n):
            ans=max(ans,a[i]-pre)
            pre=min(pre,a[i])
        print(ans)
exam23()
