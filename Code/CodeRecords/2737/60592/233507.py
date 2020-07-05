nums = input()
nums_new = nums[1:len(nums)-1].split(',')
nums_new.sort()
count = int(len(nums_new)/3)
res = []
for i in range(0,len(nums_new)-count):
    if nums_new[i] == nums_new[i+count]:
        res.append(int(nums_new[i]))
        j = i+count
        while nums_new[i] == nums[j]:
            j += 1
        i = j-1
print(res)
