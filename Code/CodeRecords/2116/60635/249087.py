n = int(input())
primes=[int(x) for x in input().split(',')]
the_ugly=[]

def isugly(num,primes):
    if num == 1:
        return True
    for prime in primes:
        while num%prime==0:
            num /= prime
    return num==1

curr = 1
while len(the_ugly)<n:
    if isugly(curr,primes):
        the_ugly.append(curr)
    curr += 1
print(the_ugly[-1])