
n=int(input())

if 1<=n<=9:
    print(n)
elif 10<=n<=9+90*2:
    n-=9
    if n%2==0:
        n/=2
        x=9+n
        print(str(x)[1])
    else:
        n=int(n/2)+1
        x=9+n
        print(str(x)[0])
else:   # 三位数
    n-=189
    if n%3==0:
        n/=3
        x=99+n
        print(str(x)[2])
    elif n%3==1:
        n=int(n/3)+1
        x=99+n
        print(str(x)[0])
    else:
        n=int(n/3)+1
        x=99+n
        print(str(x)[1])
