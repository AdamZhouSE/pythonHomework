def ad (n):
    re=int(n/2)+int(n/3)+int(n/4)
    if(re>=n):
        return re
    else:
        return n

def func(n):
    if(ad(int(n/2))==int(n/2) and ad(int((n/3)))==int(n/3) and ad(int(n/4))==int(n/4)):
        return int(n/2)+int(n/3)+int(n/4)
    else:
        return ad(int(n/2))+ad(int(n/3))+ad(int(n/4))
n=int(input())
for i in range(n):
    s=int(input())
    print(func(s))