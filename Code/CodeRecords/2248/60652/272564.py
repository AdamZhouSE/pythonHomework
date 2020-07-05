N=int(input())
A=int(input())
B=int(input())
A,B=min(A,B),max(A,B)
if B%A==0:
    print(N*A)
else:
    nA,nB=1,1
    a=[]
    index=1
    while index<=N:
        while A*nA<B*nB:
            a.append(A*nA)
            nA+=1
            index+=1
            if index==N:
                break
        a.append(B * nB)
        nB+=1
        index+=1
    print(a[N-1])