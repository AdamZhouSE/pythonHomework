nums=input()
count=0
for x in range(0,len(nums)):

    for j in range(x+1, len(nums)):
        if nums[x]>2*nums[j]:
            count+=1
print(count)         