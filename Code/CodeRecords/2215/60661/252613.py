nums=input().split(',')
nums=[int(x) for x in nums]
#偶数希望后面结果小，奇数希望后面结果大
# rec=[]
# for i in range(2,len(nums)):
#     j=len(nums)-i-1
#     if j%2==0:
s=str(nums[0])+'/('
for i in range(1,len(nums)-1):
    s=s+str(nums[i])+'/'
s+=str(nums[len(nums)-1])+')'
print(s)