def P(N):
    if(N>2):
        return P(N-2)+P(N-3);
    else:
        return 1;

Total=int(input());
i=0;
while(i<Total):
    N=int(input());
    print(P(N));
    i+=1;