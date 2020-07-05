def can(nums):
    a = int(nums[0])
    b = int(nums[1])
    if a < b*(b+1)/2:
        return 0
    else:
        return 1



total = int(input())
res = []
for i in range(total):
    nums = input().split(" ")
    res.append(can(nums))
for i in range(total):
    print(res[i])