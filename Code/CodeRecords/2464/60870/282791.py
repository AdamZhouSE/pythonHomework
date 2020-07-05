s = int(input())
nums = input().split(',')
nums = [int(x) for x in nums]
len_dict = {}
for i in range(len(nums)):
    sum_s = nums[i]
    j = i
    if sum_s > s:
        continue
    elif sum_s == s:
        len_dict[1] = 1
        break
    while sum_s < s and j < len(nums) - 1:
        j = j + 1
        sum_s = sum_s + nums[j]
    if sum_s == s:
        len_dict[j - i + 1] = 1
if len(len_dict) == 0:
    print(0)
else:
    minLen = min(len_dict.keys())
    print(minLen)