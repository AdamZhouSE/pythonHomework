nums=list(map(int,input().strip("[").strip("]").split(",")))
i=0
result=[]
while(i<len(nums)):
    if nums[i]%2==0:
        result.append(nums[i])
        del nums[i]
        i-=1
    i+=1
result.extend(nums)
print(result)
        