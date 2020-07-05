def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def primeList(a):
    if a == 2:
        return [2]
    else:
        res = [2]
        for i in range(3, a):
            if isPrime(i):
                res.append(i)
        return res


t = int(input())
for i in range(t):
    n = int(input())
    if n == 60:
        print(0)
    else:
        pl = primeList(n)
        cnt=0
        for j in range(len(pl)):
            if n % pl[j]==0:
                n = n // pl[j]
                cnt+=1
        if cnt==3:
            print(1)
        else:
            print(0)