n=int(input())
nums=input().split(' ');nums=[int(x) for x in nums]
nums.sort()
count=0;line=0
for i in range(n):
    if nums[i]>=0:
        line=i
        break
if line>0:
    for i in range(line-1):
        count+=-1-nums[i]
    if line%2==0:
        count+=-1-nums[line-1]
    elif nums.count(0)!=0:
        count+=-1-nums[line-1]
        count+=1
        line+=1
    else :
        count+=1-nums[line-1]
    for i in range(line,n):
        count+=abs(nums[i]-1)
else:
    for i in range(n):
        count+=abs(nums[i]-1)
print(count)