n = int(input())
nums =input().split(' ')
for i in range(0,n):
    nums[i]=int(nums[i])
result =0
for i in range(1,n-1):
    a =0
    b =0
    for j in range(0,i):
        if nums[j]<nums[i]:
            a+=1
    for j in range(i+1,n):
        if nums[j]>nums[i]:
            b+=1
    result +=a*b
print(result,end='')