a=int(input())
for i in range(a):
    b=int(input())
    c=input().split()
    for d in range(b):
        c[d]=int(c[d])
    c.sort()
    res=0
    for e in range(b):
        for j in range(e,b+1):
            if j<=c[e] and b-e>=j and res<j:
                res=j
    print(res)
