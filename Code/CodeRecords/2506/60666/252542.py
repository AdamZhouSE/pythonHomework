nums=list(map(int,input().strip().split(",")))
result=[1]
for i in range(1,len(nums)):
    maximum=1
    for j in range(0,i):
        if nums[i]>nums[j]:
            maximum=max(maximum,result[j]+1)
    result.append(maximum)
print(max(result))