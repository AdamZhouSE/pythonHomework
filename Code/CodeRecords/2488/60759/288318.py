nums = sorted(eval(input()))
ans = [nums[0]]
mid = (len(nums) - 1) // 2 + 1
min_ns = sorted(nums[1: mid])
max_ns = sorted(nums[mid:])
is_max = True
i, j = 0, 0
while len(ans) < len(nums):
    if is_max:
        ans.append(max_ns[i])
        i += 1
    else:
        ans.append(min_ns[j])
        j += 1
    is_max = not is_max
print(ans)
