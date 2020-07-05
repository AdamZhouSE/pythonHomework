nums = list(map(int,input().split(",")))
k = eval(input())
nums.sort()
if(k == 0):
    print(nums[-1] - nums[0])
else:
    average = sum(nums)/len(nums)
    for x in range(len(nums)):
        if(nums[x] > average):
            nums[x] -= k
        else:
            nums[x] += k
    nums.sort()
    print(nums[-1] - nums[0])