nums=input()
max1=0
count=1
if len(nums)==0:
    print(0)
for x in range(0,len(nums)-1):
    if nums[x]<nums[x+1]:
        count+=1
    else:
        max1=max(max1, count)
        count=1
max1=max(max1, count)
print( max1 )