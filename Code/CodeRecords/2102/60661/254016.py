import math
def isPrim(num):
    if num <= 3:
        return num > 1
    sqrt = int(math.sqrt(num))
    for i in range(2, sqrt+1):
        if num % i == 0:
            return False
    return True

n=int(input())
res=0
for i in range(2,n):
    if isPrim(i):
        res+=1
print(res)