nums=[int(x) for x in input().split(',')]
print(sum(range(len(nums)+1))-sum(nums))