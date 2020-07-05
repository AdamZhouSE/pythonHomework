import math
n = int(input())
judge =False

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

while(judge==False):
    if isPrime(n):
        str1 = str(n)
        str2 = ''.join(reversed(str1))
        if str1==str2:
            judge =True
    n+=1
    
print(str1)