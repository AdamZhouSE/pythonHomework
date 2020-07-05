nums=eval(input())
list.sort(nums)
result=1
record=1
for i in range(1,len(nums)):
    if(nums[i]==nums[i-1]+1):
        record+=1
    else:
        if(record>result):
            result=record
            record=1
print(result)