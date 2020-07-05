def cal(nums):
    nums = "".join(nums.split(" "))
    nums = list(map(int,list(nums)))
    max = 0
    for x in range(len(nums)):
        for y in range(x + 1,len(nums)):
            high = min(nums[x],nums[y])
            if(high * (y - x) > max):
                max = high * (y - x)
    return max

n = eval(input())
while(n != 0):
    n = n - 1
    input()
    print(cal(input()))