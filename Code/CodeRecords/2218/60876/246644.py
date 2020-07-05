nums=list(map(int,input().split(",")))
max=0
for i in range(0,len(nums)-2):
    if nums[i]*nums[i+1]*nums[i+2]>max:
        max=nums[i]*nums[i+1]*nums[i+2]
print(max)