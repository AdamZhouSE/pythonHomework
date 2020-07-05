nums=eval(input())
result=0
length=len(nums)
for start in range(0,length):
    for cmp in range(start+1,length):
        if nums[start]>2*nums[cmp]:
            result+=1
print(result)