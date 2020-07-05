nums=[int(x) for x in input().split(',')]
print([sum(nums)-sum(set(nums)),sum(range(1,len(nums)+1))-sum(set(nums))])