import math
def isPerfectNum(num):
    sum = 1
    if(num==1):
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if(num%i==0):
            sum = sum + i + num/i
    if(math.sqrt(num)**2==num):
        sum = sum +math.sqrt(num)
    return num==sum

num = int(input())
print(isPerfectNum(num))