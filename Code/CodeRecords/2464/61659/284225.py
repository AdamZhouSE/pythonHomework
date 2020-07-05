s=int(input())
nums=eval("["+input()+"]")
res=len(nums)
a=True

for i in range(0,len(nums)):
    for j in range(i+1,len(nums)+1):
        if sum(nums[i:j])>=s:
            res=min(res,j-i)
            a=False

if a:
    res=0
print(res)


