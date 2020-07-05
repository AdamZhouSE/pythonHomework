nums=eval(input())
target=int(input())
res=-1
for i in range(len(nums)):
    if(nums[i]==target):
        res=i
        break
print(res)