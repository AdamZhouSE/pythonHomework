nums = eval(input())
target = int(input())
for i in range(0,len(nums)):
    if nums[i]==target:
        print(i)
        break
    if i == len(nums)-1:
        print(-1)
    