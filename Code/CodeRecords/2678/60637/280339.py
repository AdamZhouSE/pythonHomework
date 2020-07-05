tests=(int)(input())
for i in range(tests):
    n=(int)(input())
    exist=False
    location=1
    while(n>0):
        if(n&1):
            if(exist==False):
                exist=True
            else:
                exist=False
                break
        else:
            location+=1
        n >>= 1
    if(exist):
        print(location)
    else:
        print(-1)