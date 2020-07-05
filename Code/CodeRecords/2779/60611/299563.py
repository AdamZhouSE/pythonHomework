num=int(input())

def gcd(a,b):
    c=b%a
    while c!=0:
        d=c
        c=a%c
        a=d
    return a

for i in range(num):
    t=input()
    t=sorted(list(map(int,input().split(" "))))
    a=t[0]
    b=t[-1]
    e=gcd(a,b)
    print(a*b//e)