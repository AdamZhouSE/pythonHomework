def f(nums):
    nums.sort()
    day=1
    idx=0
    while True:
        if nums[idx]>=day:
            day+=1
            idx+=1
        else:
            idx+=1
        if idx==len(nums): break
    return day-1
input()
nums=[int(x) for x in input().split()]
print(f(nums))