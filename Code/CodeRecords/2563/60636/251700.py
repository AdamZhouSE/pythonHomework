n=int(input()[1:-1])
s=60
while(True):
    print(0)
    if (pow(int(pow(n,1/s)),s)-1)/(int(pow(n,1/s))-1)==n:
        print(int(pow(n,1/s)))
        break
    else:
        s=s-1