nums=eval(input())
def func(i,j):
    return nums[i]>2*nums[j]
count=0
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if(func(i,j)):
            count+=1
print(count)