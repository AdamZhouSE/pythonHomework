def cal(temp):
    nums = list(map(int,temp.split(" ")))
    max = nums[0]
    high = 0
    for x in range(len(nums)):
        high = nums[x]
        for y in range(x + 1,len(nums)):
            if(nums[y] < high):
                high = nums[y]
            if(high * (y - x + 1) > max):
                max = high * (y - x +1)
    return max

n = eval(input())
while(n != 0):
    n = n - 1
    input()
    print(cal(input()))