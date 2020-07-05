number=int(input())
i=number
while(i>=number):
    for a in range(2,i):
        if(i%a==0):
            break
    else:
        a=list[str(i)]
        b=a.copy()
        a.reverse()
        if(a==b):
            print(i)
            break
    i+=1
            