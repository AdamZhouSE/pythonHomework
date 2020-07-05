s = input().split(',')
nums=[]
for i in range(0,len(s)):
    nums.append(int(s[i]))

count1= 0
count2 =0

for i in range(0,len(nums)-1):
    for j in range(i,len(nums)):
        if nums[i]>nums[j]:
            count1+=1

for i in range(0,len(nums)-1):
    if nums[i]>nums[i+1]:
        count2+=1

if count1==count2:
    print(True)
else:print(False)