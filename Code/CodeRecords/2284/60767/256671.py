def ans(nums):
    res = 0
    for i in range(0,len(nums)):
        for j in range(0,i):
           if(nums[i]>nums[j]):
               res = max(res,(i-j))
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