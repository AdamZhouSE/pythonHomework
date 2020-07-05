def isPrime(x):
    for i in range(2, x):
        if x%i==0:
            return False
    return True

n=int(input())
for i in range(n):
    line=input().split()
    num=list(map(int, line))
    c=1
    s=sum(num)+c
    while not isPrime(s):
        c=c+1
        s=s+1
    print(c)
    