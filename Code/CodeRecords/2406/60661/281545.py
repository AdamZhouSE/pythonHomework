n=eval(input())
nums=[]
for i in range(n):
    nums.append(eval(input()))
res=0
for i in range(n-1):
    for j in range(i+1,n):
        if nums[i]>nums[j]:
            res+=1
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
print(res)