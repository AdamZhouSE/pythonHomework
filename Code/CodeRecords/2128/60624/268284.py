def func16():
    nums = list(map(int, input().split(",")))
    Sum=pre=cur=Max=0
    for i in range(0,len(nums)):
        Sum += nums[i]
        pre += i*nums[i]
    Max = pre
    for i in range(1,len(nums)):
        cur = pre-Sum+len(nums)*nums[i-1]
        Max = max(Max,cur)
        pre = cur
    print(Max)
    return
func16()