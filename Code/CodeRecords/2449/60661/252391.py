nums=input().split(',')
nums=[int(x) for x in nums]
target=int(input())
if nums.count(target)==0:
    print(-1)
else:
    print(nums.index(target))