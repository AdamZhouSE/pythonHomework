def sumAll(nums):
    max = 0
    temp = 0
    for num in nums:
        if(num != -1):
            temp += num
        else:
            if(temp > max):
                max = temp
            temp = 0
    if(temp > max):
        max = temp
    return max

n = eval(input())
nums = list(map(int,input().split(" ")))
orders = list(map(int,input().split(" ")))

for order in orders:
    nums[order - 1] = -1
    print(sumAll(nums))