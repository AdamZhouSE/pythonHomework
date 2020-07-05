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


n = int(input())
for i in range(n):
    n = int(input())
    Sum=0
    for i in primes():
        if i>n:
            break
        if n % i ==0:
            if n % (i*i) ==0:
                Sum=-1
                break
            else:
                n=n//i
                Sum+=1
    if Sum==3:
        print(1)
    else:
        print(0)