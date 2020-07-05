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
    start = int(nums.split(' ')[0])
    end = int(nums.split(' ')[1])
    store=[]
    for i in range(start, end+1):
        if isPrim(i):
            store.append(str(i))
    print(' '.join(store))