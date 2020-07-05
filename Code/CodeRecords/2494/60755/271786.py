string = input()
nums = string[1:-1].split(",")
res = 0
for i in range(len(nums)):
    for k in range(i+1,len(nums)):
        if int( nums[i]) > 2*int(nums[k] ):
            res = res + 1
print(res)