str1=input()
nums=range(len(str1)+1)
a=[0]*(len(str1)+1)
for j in range(len(str1)):
    if str1[j]=='D':
        a[j]=max(nums)
    else:
        a[j]=min(nums)
    del nums(a[j])
print(a+nums)    
        