nums = eval(input())

longest = 0
idx = 0
while idx < len(nums):
    tmp = [nums[idx]]
    length = 1
    idx += 1
    if idx > len(nums)-1:
        longest = max(longest,length)
        break
    else:
        while nums[idx] > nums[idx-1]:
            tmp.append(nums[idx])
            idx += 1
            if idx > len(nums) - 1:
                longest = max(longest, length)
                break
        longest = max(longest,len(tmp))
print(longest)