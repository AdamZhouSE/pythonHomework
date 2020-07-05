def oddSeq():
    n=1
    while True:
        n+=2
        yield n

def notDivisivle(n):
    return lambda x:x%n>0

def primes():
    yield 2
    seq=oddSeq()
    while True:
        n=next(seq)
        yield n
        seq=filter(notDivisivle(n),seq)

def palin(n):
    s1=str(n)
    s2=s1[::-1]
    if s1==s2:
        return True
    return False


n=int(input())
for i in primes():
    if i>=n and palin(i):
        print(i)
        break