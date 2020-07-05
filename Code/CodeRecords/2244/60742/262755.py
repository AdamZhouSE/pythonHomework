import math

def isPalindrome(n):
    n_str = str(n)
    n_reversed_str = n_str[::-1]
    if n_str==n_reversed_str:
        return True
    else:
        return False

def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

n = int(input())
while isPalindrome(n)==False or isPrime(n)==False:
    n += 1
print(n)