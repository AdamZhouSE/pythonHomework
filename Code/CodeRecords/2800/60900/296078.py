r1 = input().split(' ')
n = int(r1[0])
b = int(r1[1])
nums = input().split(' ')
for i in range(0,n):
    nums[i]=int(nums[i])
count = 0
for i in range(1,n):
    while(nums[i-1]>=nums[i]):
        nums[i]+=b
        count+=1
print(count)