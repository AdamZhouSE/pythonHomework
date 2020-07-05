number=int(input())
i=number
while(i>=number):
    for a in range(2,i):
        if(i%a==0):
            i=i+1
            break
    else:
        x=list(str(i))
        b=x.copy()
        x.reverse()
        if(a==b):
            print(i)
            break
    i+=1
            