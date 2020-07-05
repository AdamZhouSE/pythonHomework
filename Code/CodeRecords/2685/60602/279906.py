def sumS(strBase):
    i=0;
    count=0;
    while(i<len(strBase)):
        count+=int(strBase[i]);
        i+=1;
    return count;
def sumN(N):

    base=10**N;
    temp=base;
    while(True):
        base=base+temp;
        strBase=str(base);
        if(sumS(strBase)==N):
            print(strBase);
            return


Total=int(input());
i=0;
while(i<Total):
    N=int(input());
    sumN(N);
    i+=1;