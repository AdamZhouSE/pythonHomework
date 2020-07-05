nums=list(map(int,input().split(',')))
target=int(input())
if target in nums:
    print(nums.index(target))
else:
    i=0
    while True:
        if target>nums[len(nums)-1]:
            print(len(nums))
            break
        elif target<nums[0]:
            print(0)
            break
        else:
            if nums[i]<target and nums[i+1]>target:
                print(i+1)
                break
            else:
                i+=1