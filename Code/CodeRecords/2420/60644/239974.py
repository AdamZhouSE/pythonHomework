n=int(input())
s1=True
s2=True
for a in range(1,n):
    b=n-a
    a2=a
    b2=b
    while a2>0:
        a1=a2%10
        a2=int(a2/10)
        if a1==0:
            s1=False
            break
    while b2>0:
        b1=b2%10
        b2=int(b2/10)
        if b1==0:
            s2=False
            break
    if s1 and s2:
        print([a]+[b])
        break
    s1=s2=True
