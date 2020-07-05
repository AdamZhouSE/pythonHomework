def ans(nums,lower,upper):
    cnt = 0
    for i in range(len(nums)):
        for j in range(i+1):
            temp = sum(nums[j:i+1])
            if(temp>=lower and temp<=upper):
                cnt += 1
    return cnt

temp = eval(input())
nums = []
for t in temp:
    nums.append(int(t))
lower = int(input())
upper = int(input())
print(ans(nums,lower,upper))