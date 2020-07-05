nums=input()
max=0
count=1
if len(nums)==0:
    print(0)
for x in range(0,len(nums)-1):
    if nums[x]<nums[x+1]:
        count+=1
    else:
        max=max(max, count)
        count=1
max=max(max, count)
print( max )