n=int(input()[1:-1])
print(n)
s=60
while(True):
    if(int(pow(n,1/s))==pow(n,1/s)):
        if (pow(int(pow(n,1/s)),s)-1)/(int(pow(n,1/s))-1)==n:
            print(int(pow(n,1/s)))
        break
    else:
        s=s-1