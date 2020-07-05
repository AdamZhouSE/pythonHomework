def ans(nums):
    res = -1
    for i in range(0,len(nums)-1):
        if(nums[i] in nums[i+1:]):
            res = i+1
            break
    return res

numOfTests = int(input())
temp = []
for i in range(numOfTests):
    n = int(input())
    nums = []
    temp = input().split(" ")
    for t in temp:
        nums.append(int(t))
    print(ans(nums))