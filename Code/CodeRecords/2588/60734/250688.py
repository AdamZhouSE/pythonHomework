import math                                                       
def Smith(x):
    parts = [] #存放分解的数字
    sum_x = sum(list(map(int,str(x))))
    prime = 2
    while x>1:
        if isPrime(x):
            parts.append(x)
            break
        while x%prime == 0:
            x /= prime
            parts.append(prime)
        prime = getNextPrime(prime)
    sum_parts = 0
    for x in parts:
        while x>0:
            sum_parts+=x%10
            x = x//10
    return sum_parts == sum_x
        
def isPrime(x):
    for i in range(2,int(x)):
        if x%i == 0:
            return False
    return True

def getNextPrime(i):
    number = i+1
    while isPrime(number) == False:
        number+=1
    return number
                 
  
t = int(input())
lst = []
for i in range(t):
    lst.append(int(input()))
for x in lst:
    if Smith(x):
        print('1')
    else:
        print('0')