import math
def isPrime(num):
    high = int(math.sqrt(num)) + 1
    for x in range(2,high):
        if(num % x == 0):
            return False
    return True

def find(num):
    if(num == 1):
        return [1]
    if(isPrime(num)):
        return [1,num]
    result = [1]
    n = num
    for x in range(2,num + 1):
        while(n % x == 0):
            n = int(n/x)
            result.append(x)
            if(n == 1):
                return result
def get(result):
    dict = {}
    for res in result:
        if res in dict:
            dict[res] += 1
        else:
            dict[res] = 1
    res = 1
    for m in dict.keys():
        res *= dict[m] + 1
    return int(res/2)

def getSim(result,temp):
    res = []
    i = j = 0
    while(i < len(result) and j < len(temp)):
        if(result[i] == temp[j]):
            res.append(result[i])
            i = i + 1
            j = j + 1
        else:
            if(result[i] == result[i-1]):
                i = i + 1
            else:
                j = j + 1
    return res

def cal(nums):
    nums = list(map(int,nums))
    nums.sort()
    result = find(nums[0])
    for m in range(1, len(nums)):
        temp = find(nums[m])
        result = getSim(result,temp)
    return get(result)

input()
nums = input().split(" ")
print(cal(nums))
