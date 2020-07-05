nums=eval(input())
num_index=[0 for i in range(len(nums))]
res=0
for i in range(len(nums)):
    num_index[nums[i]]=i
for i in range(len(nums)):
    if i==0 :
        if num_index[i]==0:
            res+=1
    elif max(num_index[:i])<=i:res+=1
print(res)