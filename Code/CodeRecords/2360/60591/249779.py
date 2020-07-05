import math
def isSquare(num):
    if(int(math.sqrt(num)) == math.sqrt(num)):
        return True
    else:
        return False

def isValid(nums):
    for x in range(len(nums) - 1):
        number = nums[x] + nums[x + 1]
        if(not isSquare(number)):
            return False
    return True

def generate(nums,n,result):
    if(n == 0):
        if(isValid(result)):
            if(result not in a):
                a.append(result)
                return 1
            else:
                return 0
        else:
            return 0
    else:
        res = 0
        for c in nums:
            temp1 = nums.copy()
            temp2 = result.copy()
            temp2.append(c)
            temp1.remove(c)
            res += generate(temp1,n - 1,temp2)
        return res

n = list(map(int,input().split(",")))
length = len(n)
a = []
print(generate(n,length,[]))
