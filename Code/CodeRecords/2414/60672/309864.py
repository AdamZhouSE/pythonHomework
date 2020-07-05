import decimal
def right(n):
    if n==1:
        return 1.0
    p=[0 for i in range(10000)]
    p[1]=1.0
    p[2]=0.5
    for i in range(3,n):
        p[i]=1.0/i
        for k in range(2,i):
            p[i]+=p[i-k+1]/i
    return p[n]

def accurate(n):
    n=round(n,5)
    n=str(n)
    if len(n)==3:
        n=n+'0000'
        return n
    elif len(n)==7:
        print(n)
        return n
    else:
        print(n)
        for i in range(7-len(n)):
            n=n+'0'
        return n
n=int(input())
answer=float(right(n))
answer=accurate(answer)
print(answer)