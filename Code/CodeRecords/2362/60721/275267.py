n=int(input())
if n<3:
    print(n)
elif n==3:
    print(6)
elif n==4:
    print(7)
else:
    count=0
    re=0
    summ=n
    for i in range(0,n-1):    
        a=i%4
        if a==0:
            summ=summ*(n-1-i)
        elif a==1:
            summ=int(summ/(n-i-1))
        elif a==2:
            if i==2:
                re+=summ
            else:
                re-=summ
            summ=n-1-i            
        else:            
            re+=summ
            summ=n-i-1
            if i==n-2:
                re=re-(n-i-2)
    print(int(re-summ))

        