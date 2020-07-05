def getComDiv(p, q):
    while p != q:
        if p > q:
            p = p - q
        else:
            q = q - p
    return q

def factorization(num):
    factor = []
    while num > 1:
        for i in range(num - 1):
            k = i + 2
            if num % k == 0:
                factor.append(k)
                num = int(num / k)
                break
    return factor

def isValid(n, list):
    for i in range (len(list)):
        if n % list[i] == 0:
            return True
    return False

def getStep(a, b):
    if b == 1:
        return a - 1
    elif b == 0:
        return 100
    else:
        return a // b + getStep(b, a % b)

def getNlist(n):
    if n == 1:
        return 0
    l = []
    fac = factorization(n)
    for i in range (1, int(n/2 + 1)):
        if isValid(i, fac) == False:
            l.append(getStep(n, i))
    return int(min(l))

if __name__ == '__main__':
    n = int(input())
    a = getNlist(n)
    print(a, end='')
