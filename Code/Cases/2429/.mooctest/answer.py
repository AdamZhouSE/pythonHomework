t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    s=input().split(' ')
    if '' in s:
        s.remove('')
    i=n-2
    s[n-1]=int(s[n-1])
    s[0]=int(s[0])
    a=[0 for i in range(n) ]
    a[n-1]=s[n-1]
    while(i>0):
        s[i]=int(s[i])
        a[i]=max(s[i],a[i+1])
        i-=1
    o=-1
    for i in range(n-1):
        o=max(a[i+1]-s[i],o)
    print(o)