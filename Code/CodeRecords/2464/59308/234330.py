s = int(input())
nums = [int(x) for x in input().split(",")]
nums.sort()
min_ = 100000000
index = 0
for i in range(len(nums)):
    if abs(s-nums[i]) <= min_:
        min_ = abs(s-nums[i])
        index = i
min_ = nums[index]
if min_ == 0:
    print(1)
else:
    for i in range(index+1, len(nums)):
        min_ = min_ + nums[i]
        if min_ >= s:
            print(i - index)
            break
    if min_ < s:
        for i in range(index-1, -1 , -1):
            min_ = min_ + nums[i]
            if min_ >= s:
                print(len(nums)-i)
                break
