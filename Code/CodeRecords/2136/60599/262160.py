n=int(input())
i=2
while 1:
    k = n
    while 1:
        if(k%i==1):
            k//=i
            if(k==1):
                print(i)
                exit()
        else:break
    i+=1
