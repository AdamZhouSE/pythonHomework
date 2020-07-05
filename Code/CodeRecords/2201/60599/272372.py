def zs(n):
    for i in range(2,n//2+2):
        if(n%i==0):
            return False
    return True
u=int(input())
for p in range(u):
    s=list(map(int,input().split(' ')))
    sum=s[0]+s[1]
    k=1
    while 1:
        if(zs(k+sum)):
            print(k)
            break
        k+=1
        