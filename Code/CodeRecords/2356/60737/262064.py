t = int(input())
while t:
    l = int(input())
    nums = [int(n) for n in input().split( )]
    ret = -1
    if min(nums[1:]) >= nums[0]:
        ret = nums[0]
    i = 1
    for i in range(1, l-1):
        if max(nums[:i])<nums[i] and min(nums[i+1:])>=nums[i]:
            ret = nums[i]
            break
    print(ret)
    t -= 1
   