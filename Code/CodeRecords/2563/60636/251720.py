n=int(input()[1:-1])
s=59
while(True):
    if(int(pow(n,1/s))!=1):
        if (pow(int(pow(n,1/s)),s+1)-1)/(int(pow(n,1/s))-1)==n:
            print(int(pow(n,1/s))-1)
            break
    elif(int(pow(n,1/s))==1):
        s=s-1
    else:
        s=s-1