def ans(nums):
    cnt = 0
    right = 0
    left = 1
    while(left<=len(nums)):
        temp = nums[right:left]
        temp.sort()
        if(temp==[i for i in range(right,left)]):
            cnt += 1
            right = left
            left = right + 1
        else:
            left += 1
    return cnt

temp = eval(input())
nums = []
for t in temp:
    nums.append(int(t))
print(ans(nums))
