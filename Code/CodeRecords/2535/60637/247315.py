nums=eval(input())
nums_sorted=sorted(nums)
start=0
result=0
for i in range(0,len(nums)):
    end=i+1
    setnums=set(nums[start:end])
    setnums_sorted=set(nums_sorted[start:end])
    if(setnums.issubset(setnums_sorted)&setnums.issuperset(setnums_sorted)):
        result+=1
        start=i+1
print(result)
