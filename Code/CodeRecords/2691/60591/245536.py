def cal(nums):
    nums = list(map(int,nums.split(" ")))
    nums.sort(reverse=True)
    sum1 = nums[0]
    sum2 = 0
    for x in range(1,len(nums)):
        if(sum1 > sum2):
            sum2 += nums[x]
        else:
            sum1 += nums[x]
    return (abs(sum1 - sum2))

n = eval(input())
while(n != 0):
    n = n - 1
    input()
    nums = input()
    res = cal(nums)
    print(res)