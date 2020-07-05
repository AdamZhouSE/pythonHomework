n=int(input())
a=list(map(int,input().split(' ')))
a.sort()
b=set(a)
if len(b)>3:
    print(-1)
else:
    if len(b)==1:
        print(0)
    elif len(b)==2:
        dis=a[len(a)-1]-a[0]
        if dis%2==0:
            print(dis//2)
        else:
            print(dis)
    elif len(b)==3:
        mid=(a[0]+a[len(a)-1])/2
        if mid in a:
            print(int(mid-a[0]))
        else:
            print(-1)