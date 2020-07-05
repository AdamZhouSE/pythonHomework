n=int(input())
nums=input().split(" ")
nums[0]=int(nums[0])
for i in range(1,n):
    nums[i]=nums[i-1]+int(nums[i])
m=int(input())
serial=input().split(" ")
for i in range(m):
    serial[i]=int(serial[i])
result=[]
nums.insert(0,0)
for i in range(m):
    for j in range(n):
        if serial[i]>nums[j] and serial[i]<=nums[j+1]:
            result.append(j+1)
for i in range(len(result)):
    print(result[i])