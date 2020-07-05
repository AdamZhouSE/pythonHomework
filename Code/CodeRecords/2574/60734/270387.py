import math
def isPrime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True

def f(x):
    base = 1
    while x>0:
        base+=1
        if isPrime(base):
            x = x-1
    return base**2+1
    
t = int(input())
for i in range(t):
    print(f(int(input())))