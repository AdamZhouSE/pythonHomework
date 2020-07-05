nums = [int(x) for x in input().split(",")]
nums.sort(reverse=True)
flag = True
for i in range(0, len(nums) - 2):
    if nums[i] + nums[i + 1] <= nums[i + 2] or nums[i + 1] + nums[i + 2] <= nums[i] or nums[i] + nums[i + 2] <= nums[i + 1]:
        continue
    else:
        print(nums[i] + nums[i + 1] + nums[i + 2])
        flag = False
        break
if flag:
    print(0)
