str1=input()
nums=[i for i in range((str1)+1)]
a=[0]*(len(str1)+1)
for j in range(len(str1)):
    if str1[j]=='D':
        a[j]=max(nums)
        nums.remove(max(nums))
    else:
        a[j]=min(nums)
        nums.remove(min(nums))
print(a+nums)    
        