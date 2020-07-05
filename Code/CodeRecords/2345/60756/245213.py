n=int(input())
for i in range(n):
    m=int(input())
    a=list(map(int,input().split()))
    a.sort(key=int)
    ans=[0,0]
    for i in a:
        if ans[0]==0:
            if a.index(i)<len(a)-1:
                if a[a.index(i)+1]==i:
                    ans[0]=i
                    a.remove(i)
        if ans[1]==0:
            if i!=a.index(i)+1:
                ans[1]=a.index(i)+1
                a.insert(a.index(i),a.index(i)+1)
    ans=list(map(str,ans))
    print(' '.join(ans))