def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True


def isReturn(n):
    l = len(n)//2*2
    for i in range(0, int(l/2)):
        if n[i]!=n[len(n)-1-i]:
            return False
    return True


n = int(input())
while True:
    if isPrime(n) and isReturn(str(n)):
        print(n)
        break
    else:
        n += 1
