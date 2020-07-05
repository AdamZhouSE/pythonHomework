def numN(N):
    for i in range(1,1000):
        n=N/(10**i)
        if n<1:
            break
    return i
def arrayN(N):
    n=numN(N)
    newN=[]
    s=0
    for i in range(0,n):
        k=10**(n-1-i)
        t=int((N-N%k)/k)
        newN.append(t-s*10)
        s=t
    return(newN)
def TF(N):
    A=arrayN(N)
    n=numN(N)
    a=10**(n-1)
    b=10**n
    new=[]
    result=1
    for i in range(1,4*n):
        if a<2**i<b:
            new.append(i)
        if 2**i>b:
            break
    n1=len(new)
    for j in range(0,n1):
        k=2**(new[j])
        B=arrayN(k)
        for t in range(0,n):
            if A[t] in B:
                result=1
            else:
                result=0
                break
        if result==1:
            break
    if N==1:
        return True
    elif result==1:
        return True
    else:
        return False
N=1
print(TF(N))
    
            
            
            