n=int(input())
nums=input().split(" ")
for i in range(n):
    nums[i]=int(nums[i])

max=0
this = 1
index=0
if n==1:max=1
while index<n-1:
    if nums[index]<nums[index+1]:
        this+=1
        if index==n-2 and max <this:
            max=this
    else:
        if max<this: max=this
        this=1
    index+=1
print(max)
if max==0:print(nums)