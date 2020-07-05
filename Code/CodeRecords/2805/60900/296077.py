n = int(input())
nums = input().split(' ')
for i in range(0,n):
    nums[i] = int(nums[i])
result = 1
temp=1
i =0

while(i!=n-1):
    if nums[i+1]>nums[i]:
        temp +=1
        i+=1
    else :
        result= max(result,temp)
        temp=1
        i+=1
    if i==n-1:
        result = max(result,temp)

print(result)