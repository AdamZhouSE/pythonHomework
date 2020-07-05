number=int(input())
i=number
while(i>=number):
    su=True
    for a in range(2,i):
        if(i%a==0):
            su=False
    if(su):
        x=list(str(i))
        b=x.copy()
        x.reverse()
        if(x==b):
            print(i)
            break
        else:
            i=i+1
    else:
        i=i+1
            