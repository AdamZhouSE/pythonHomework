n=int(input()[1:-1])
print(n)
s=59
while(s>=0):
    if(int(pow(n,1/s))!=1):
        if (pow(int(pow(n,1/s)),s+1)-1)/(int(pow(n,1/s))-1)==n:
            if(int(pow(n,1/s))==pow(n,1/s)):
                print(int(pow(n,1/s))-1)
            else:
                print(int(pow(n,1/s)))
            break
        else:
            s=s-1
    elif(int(pow(n,1/s)==1)):
        print(s-1)
    else:
        s=s-1