T=int(input())
for i in range(0,T):
    n=(input())
    if(int(n)<10):
        print(n)
    else:
        while int(n) > 10:
            s=list(n)
            re=0
            for i in s:
                re+=int(i)
            n=str(re)
        print(n)