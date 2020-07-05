def test():
    t=int(input())
    for _ in range(0,t):
        mn=input().split()
        m=int(mn[0])
        n=int(mn[1])
        res=[]
        for i in range(m,n+1):
            if isPrime(i):
                res.append(i)
        res=' '.join(list(map(str,res)))
        print(res)

def isPrime(n):
    if n<=1:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        return True

test()