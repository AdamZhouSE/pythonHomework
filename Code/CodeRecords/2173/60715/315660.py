T=int(input())
while T>0:
    x=int(input())
    re=0
    l=1
    while l<=2*x-1:
        tt=1
        while tt<=l:
            re+=tt
            tt+=2
        l+=2
    print(re)
    T-=1