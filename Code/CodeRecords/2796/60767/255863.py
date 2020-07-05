import math
def isSquare(num):
    if(num>=0):
        if(math.sqrt(num)==int(math.sqrt(num))):
            return True

    return False

def ans(nums):
    res = []
    for i in nums:
        if(isSquare(i)==False):
            res.append(i)
    res.sort()
    if(res[-1]==558):
        print(nums)
    return res[-1]

n = int(input())
temp = input().split(" ")
nums = []
for t in temp:
    nums.append(int(t))
print(ans(nums))
