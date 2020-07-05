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
    nums = input()
    left = int(nums.split(' ')[0])
    right = int(nums.split(' ')[1])
    count=0
    for i in range(left,right+1):
        j=bin(i)
        if isPrim(j.count('1')):
            count+=1
    print(count)