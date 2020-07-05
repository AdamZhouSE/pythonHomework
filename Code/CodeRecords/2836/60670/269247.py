n=int(input())
a=list(map(int,input().split()))
ll=-1
for i in range(0,n-1):
    if a[i]>a[i+1]:
        ll=i
        break
if ll==-1:
    print(0)
else:
    a=a[ll+1:n]+a[0:ll+1]
    ok=True
    for i in range(0,n-1):
        if a[i]>a[i+1]:
            ok=False
            break
    if ok==True:
        print(n-ll-1)
    else:
        print(-1)