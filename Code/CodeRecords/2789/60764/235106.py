a=int(input())
for i in range(a):
    b=int(input())
    c=input().split()
    for d in range(b):
        c[d]=int(c[d])
    c.sort()
    res=c[0]
    for e in range(b):
        if c[e]>res and b-e>c[e]:
            res=c[e]
    print(res)
