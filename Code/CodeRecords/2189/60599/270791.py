def kl(n):
    k=100
    while k>0:
        tmp=0
        while n>0:
            tmp+=(n%10)**2
            n//=10
        if (tmp == 1):
            return True
        n=tmp
        k -= 1
    return False

u=int(input())
for i in range(u):
    c=int(input())
    c+=1
    while 1:
        if(kl(c)):
            break
        c+=1
    print(c)
