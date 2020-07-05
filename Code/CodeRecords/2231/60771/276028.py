#07
from itertools import permutations,combinations

def isPrime(n):
    flag = True
    for i in range(2,n):
        if n % i == 0:
            flag = False
            break
    return flag

T = int(input())
Prime = [2] #生成一百以内的质数
SphenicNum = []
for i in range(3,100):
    flag = isPrime(i)
    if flag == True:
        Prime.append(i)
PrimeGroup = list(combinations(Prime,3))
for item in PrimeGroup:
    num = item[0] * item[1] * item[2]
    SphenicNum.append(num)
for i in range(0,T):
    n = int(input())
    if n not in SphenicNum:
        print(0)
    else:
        print(1)

