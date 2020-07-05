nums = sorted(eval(input()))
ans = 0
count = 1
carry = nums[0]
for num in nums:
    if num != carry + count:
        if count > ans:
            ans = count
        count = 1
        carry = num
    else:
        count += 1
if count > ans:
    ans = count
print(ans)