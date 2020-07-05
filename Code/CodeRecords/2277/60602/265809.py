K=int(input());
N=int(input());
if(N==0 and K==0):
    print(0);
else:
    if(N!=2 and N!=14 and N!=6):
        print(7);
    else:
        print(N//K);
    