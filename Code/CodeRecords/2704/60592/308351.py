nums = eval(input())
num = [nums[0][0]]
res=[]
for i in range(0,len(nums)):
    if not nums[i][1] in num:
        num.append(nums[i][1])
    else:
        res=nums[i]
        break
print(res)