def cal(nums):
    nums = nums.split(" ")
    num1 = 0
    num2 = 0
    res = 0
    pre = nums[0]
    for x in range(len(nums)):
        if(pre == nums[x]):
            if(nums[x] == '1'):
                num1 += 1
            else:
                num2 += 1
        else:
            count = min(num1,num2) * 2
            if(count > res):
                res = count
            if(nums[x]=='1'):
                num1 = 1
            else:
                num2 = 1
            pre = nums[x]
    count = min(num1,num2) * 2
    if(count > res):
        res = count
    return res

input()
print(cal(input()))

