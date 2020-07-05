t=int(input())
for i in range(t):
    n=int(input())
    a=input().split(' ')
    a=list(map(int,a))
    ans=[]
    for j in range(n):
        temp=a[j]
        has=False
        for k in range(j+1,n):
            if a[k]>=temp:
                ans.append(a[k])
                has=True
                break
        if not has:
            ans.append(-1)
    ans=list(map(str,ans))
    print(' '.join(ans))