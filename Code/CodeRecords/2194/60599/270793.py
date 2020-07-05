def zs(n):
    if(n==1):
        return False
    if (n == 2):
        return True
    for o in range(2,n//2+2):
        if(n%o==0):
            return False
    return True
u=int(input())
for p in range(u):
    s=list(map(int,input().split(' ')))
    res=""
    for i in range(s[0],s[1]+1):
        if(zs(i)):
            res+=str(i)+" "
    print(res[:len(res)-1])