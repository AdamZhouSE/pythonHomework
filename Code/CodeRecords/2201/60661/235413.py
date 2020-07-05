import math
def isPrim(num):
    if num <= 3:
        return num > 1
    sqrt = int(math.sqrt(num))
    for i in range(2, sqrt+1):
        if num % i == 0:
            return False
    return True

t = int(input())
for i in range(t):
    ab=input()
    a=int(ab.split(' ')[0])
    b=int(ab.split(' ')[1])
    num=a+b+1
    while True:
        if isPrim(num):
            print(num-a-b)
            break
        else:
            num+=1