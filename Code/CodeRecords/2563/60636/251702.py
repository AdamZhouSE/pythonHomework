n=int(input()[1:-1])
s=59
count=0
while(True):
    count=count+1
    print(count)
    if (pow(int(pow(n,1/s)),s)-1)/(int(pow(n,1/s))-1)==n:
        print(int(pow(n,1/s)))
        break
    else:
        s=s-1