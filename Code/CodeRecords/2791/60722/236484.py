n=int(input())
nums=input().split(" ")
for i in range(n):
    nums[i]=int(nums[i])
res=[idx for idx,i in enumerate(nums) if i==1]
print(len(res))
result=""
for i in range(1,len(res)):
    result+=str(res[i]-res[i-1])
    result+=" "
result+=str(len(nums)-res[len(res)-1])
print(result[0:len(result)])