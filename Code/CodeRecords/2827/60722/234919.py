n=int(input())
nums=input().split(" ")
for i in range(n):
    nums[i]=int(nums[i])
nums.sort()
result=""
for i in range(n):
    result+=str(nums[i])
    result+=" "
print(result[0:len(result)-1])