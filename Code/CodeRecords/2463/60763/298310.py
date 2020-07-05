nums = eval('['+input()+']')
# print(nums[2])
tar = int(input())
a = []
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j] == tar:
            a.append(i+1)
            a.append(j+1)
            break
print(a)