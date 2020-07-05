def mirrorReflection(p,q):
    def common_mul(a,b):
        s=a
        while s%b!=0:
            s+=a
        return s
    cm=common_mul(p,q)
    t1=cm/q
    t2=cm/p
    while t1>1:
        t1-=2
    while t2>1:
        t2-=2
    if t1==0 and t2==1:
        return 2
    if t1==1 and t2==1:
        return 1
    if t1==1 and t2==0:
        return 0
    return -1


p=int(input())
q=int(input())
print(mirrorReflection(p,q))