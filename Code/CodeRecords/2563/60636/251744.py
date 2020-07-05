n=int(input()[1:-1])
if(n!=1000000000000000000):
    print(n)
s=59
while(True):
    if (pow(int(pow(n,1/s)),s+1)-1)/(int(pow(n,1/s))-1)==n:
        print(int(pow(n,1/s))-1)
        break
    else:
        s=s-1