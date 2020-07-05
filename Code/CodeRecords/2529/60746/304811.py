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
N=12345
print(arrayN(N))