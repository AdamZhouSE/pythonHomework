def ans(nums):
    cnt = 0
    for i in range(len(nums)):
        for j in range(i):
            if(nums[j]>2*nums[i]):
                cnt += 1
    return cnt
temp = eval(input())
nums = []
for t in temp:
    nums.append(int(t))
print(ans(nums))