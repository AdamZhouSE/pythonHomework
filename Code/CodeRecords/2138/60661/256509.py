nums=eval(input())
k=eval(input())
rec={nums[0]%k:0}
sum=nums[0]
for i in range(1,len(nums)):
    sum+=nums[i]
    if rec.get(sum%k)!=None:
        print(True)
        exit()
    else:
        rec[sum%k]=i