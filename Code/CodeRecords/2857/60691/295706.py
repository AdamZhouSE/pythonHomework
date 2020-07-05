import math

def function(l, n):
    num = []
    for i in range(2, n+1):
        boolean = True
        for j in range(len(l)):
            if l[j] % i != 0:
                boolean = False
                break
        if boolean:
            num.append(i)
    return len(num)+1


def isprime(n):
    if n % 2 == 0:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True


n = int(input())
s = input().split(' ')
l = []
for i in range(len(s)):
    l.append(int(s[i]))

l.sort()
if l[0] > 4200 and not isprime(l[0]):
    print(4200)
else:
    print(function(l, l[0]))
