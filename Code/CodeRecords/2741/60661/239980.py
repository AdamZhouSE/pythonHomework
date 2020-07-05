nums=input()[1:-1].split(',')
nums=[int(x) for x in nums]
maxlen=1;length=1
for i in range(1,len(nums)):
    if nums[i]>nums[i-1]:
        length+=1
        continue
    else:
        if length>maxlen:
            maxlen=length
        length=1
print(maxlen)