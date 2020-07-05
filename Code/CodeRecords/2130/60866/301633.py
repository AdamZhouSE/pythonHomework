def shuzi(a):
    n=9
    digits=1
    while a-n*digits>0:
        a=a-n*digits
        n=n*10
        digits=digits+1
    b=1
    i=1
    while i<digits:
        b=b*10
        i=i+1
    if a<=digits:
        c=b
    else :
        c=b+a//digits-1
    if a%digits==0:
        d='%d'%c
        return d[digits-1]
    else :
        c=c+1
        d='%d'%c
        return d[a%digits-1]
a=int(input())
print(shuzi(a))