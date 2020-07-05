#斐波那契
def fa(a):
    if a==1 or a==0:
        return 1
    n1=1
    n2=1
    re=0
    while(a!=1):
        re=n1+n2
        n1=n2
        n2=re
        a-=1
    return re
t=int(input())
for i in range(t):
    n=int(input())
    print(fa(n))