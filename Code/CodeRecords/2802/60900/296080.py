
r1 = input().split(' ')
n = int(r1[0])
m = int(r1[1])
nums = input().split(' ')
for i in range(0,n):
    nums[i]=int(nums[i])
count =0
result =0
while(result==0):
    for i in range(0,n):
        if (nums[i]>m):
            nums[i]-=m
        elif (nums[i]<=m and nums[i]!=0):
            nums[i]=0
            count+=1
        if count == n:
            result =i+1
            break


print(result)