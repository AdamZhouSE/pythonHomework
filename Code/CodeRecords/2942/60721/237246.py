x=int(input())
nums=input().split(" ")
for j in range(0,x):
    for i in range(1, len(nums)):
        if (int(nums[i - 1][0]) < int(nums[i][0])):
            temp = nums[i - 1]
            nums[i - 1] = nums[i]
            nums[i] = temp
        elif(int(nums[i - 1][0]) == int(nums[i][0])):
            if (int(nums[i - 1][1]) < int(nums[i][1])):
                temp = nums[i - 1]
                nums[i - 1] = nums[i]
                nums[i] = temp
re=""
for m in nums:
    re=re+m
print(re,end="")