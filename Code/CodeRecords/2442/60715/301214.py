num=input("")
num=num[1:len(num)-1]
nums=num.split(',')
nums=list(map(int,nums))
nums=sorted(nums)
t=0
for i in range(1,len(nums)):
    if nums[i]-nums[i-1]>t:
        t=nums[i]-nums[i-1]
print(t)