nums=input()
sum=int(nums[0])
maxsum=int(nums[0])
for i in range(1,len(nums)):
    if sum>0:
        sum=sum+int(nums[i])
    else:
        sum=int(nums[i])
    if sum>maxsum:
        maxsum=sum
print(maxsum)