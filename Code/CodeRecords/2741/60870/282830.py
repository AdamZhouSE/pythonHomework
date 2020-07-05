str_input = input()
str_valid = str_input[1:-1]
nums = str_valid.split(',')
nums = [int(x) for x in nums]
len_dict = {1:1}
for i in range(len(nums)):
    j = i
    while j < len(nums) - 1:
        j = j + 1
        if nums[j] <= nums[j - 1]:
            break
    len_valid = j - i
    len_dict[len_valid] = 1
maxLen = max(len_dict.keys())
print(maxLen)