def findErrorNums(nums):
    S = len(nums)* (len(nums)+1) // 2
    N = sum(nums)
    L = sum(set(nums))
    return [N-L,S-L]
a=input().split(',')
a=[int(x) for x in a]
print(findErrorNums(a))