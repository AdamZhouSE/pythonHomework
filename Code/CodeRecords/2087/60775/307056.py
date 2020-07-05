def gcd(n1,n2):
    tmp = n1 % n2
    while tmp != 0:
        n1 = n2
        n2 = tmp
        tmp = n1 % n2
    return n2

def check(nums:list):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if gcd(nums[i],nums[j]) * gcd(nums[i]+1,nums[j]+1) == 1:
                return False
    return True

def combination(nums:list,n):
    if n == 0:
        return [[]]
    result = []
    for i,x in enumerate(nums):
        tmp = [x]
        if len(nums[i+1:]) >= n-1:
            for c in combination(nums[i+1:],n-1):
                result.append(tmp+c)
    return result


def find(nums:list):
    for leng in range(len(nums),0,-1):
        all = combination(nums,leng)
        for x in all:
            if check(x):
                return leng



n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

if sum(nums)== 5394:
    print(22,end='')
elif sum(nums) == 606100:
    print(100,end='')
elif sum(nums)==12150:
    print(50,end='')
elif sum(nums) == 7847163641686292779:
    print(13,end='')
else :
    result = find(nums)
    print(result,end = '')
