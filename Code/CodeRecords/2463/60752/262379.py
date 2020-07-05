nums=list(map(int,input().split(',')))
sum=int(input())
found=False
for i in range(len(nums)-1):
    if found:break
    if nums[i]+nums[0]>sum:break
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==sum:
            found=True
            print([i+1,j+1])
            break
        if nums[i]+nums[j]>sum:break
if not found:print(None) 
