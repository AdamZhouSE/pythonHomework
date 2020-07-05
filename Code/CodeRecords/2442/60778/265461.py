nums=eval(input())
res=0
for i in range(len(nums)-1):
    x=nums[i+1]-nums[i]
    if(x>res):
        res=x
print(res)