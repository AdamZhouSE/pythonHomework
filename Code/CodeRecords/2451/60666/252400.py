nums=list(map(int,input().strip().split(",")))
target=int(input())
if target in nums:
    print(nums.index(target))
else:
    if target<nums[0]:
        print(0)
    elif target>nums[-1]:
        print(len(nums))
    else:
        for i in range(len(nums)-2):
            if target>nums[i] and target<nums[i+1]:
                result=i
                break
        print(result)