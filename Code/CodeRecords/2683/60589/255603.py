t=int(input())
for i in range(t):
    s=input()
    a=list(s)
    f=[1]*len(a)
    for x in range(len(a)):
        for p in range(0,x):
            if a[p]<a[x]:
                f[x]=max(f[x],f[p]+1)
    print(max(f))