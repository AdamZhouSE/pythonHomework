def test():
    t=int(input())
    for _ in range(0,t):
        mn=input().split()
        m=int(mn[0])
        n=int(mn[1])
        count=0
        for i in range(m,n+1):
            str_bin=bin(i)[2:]
            if isPrime(str_bin.count(str(1))):
                count=count+1
        print(count)

def isPrime(n):
    if n<=1:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        return True

test()