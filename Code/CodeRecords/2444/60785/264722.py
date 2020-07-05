#nums = [1,2,3,1], k = 3, t = 0
tmp = input().split("]")
ins1 = tmp[0]+']'
ins2and3= tmp[1].split(',')
ins2 = ins2and3[1][1:]
ins3 = ins2and3[2][1:]
exec(ins1)
exec(ins2)
exec(ins3)
result="false"
for i in range(len(nums)):
    for j in range(i,len(nums)):
        if i ==j:continue
        if j-i<=k:
            if nums[i] - nums[j] > 0:
                if nums[i] - nums[j] <= t :
                    result = "true"
            else:
                if nums[j] - nums[i] <= t :
                    result = "true"
print(result)
