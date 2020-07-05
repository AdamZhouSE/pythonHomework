input()
nums = input()
if(len(nums) == 1):
    print(0)
elif(len(nums) == 2):
    if(nums[0]==nums[1]):
        print(1)
    else:
        print(0)
else:
    pre = nums[0] # 不变
    now = nums[1]
    next = nums[2]
    count = 0
    for x in range(1,len(nums) - 1):
        now = nums[x]
        next = nums[x+1]
        if(now == pre):
            count += 1
        else:
            pre = now
            continue
    if(now == nums[-1]):
        count += 1
    print(count)