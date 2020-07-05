n=int(input())
nums=input().split(" ")
for i in range(n): nums[i]=int(nums[i])
res=0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if nums[i]<nums[j]<nums[k]:
                res+=1
print(res,end="")