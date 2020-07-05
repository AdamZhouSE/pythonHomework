def AorB(N,A,B):
    i=1;
    count=0;
    while(count<N):
        if(i%A==0 or i%B==0):
            count+=1;
        i+=1;
    print((i-1)%(10^9 + 7));

N=int(input());
A=int(input());
B=int(input());
AorB(N,A,B);