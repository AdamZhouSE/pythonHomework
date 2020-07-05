nums=eval(input())
n=int(input())
res=-1
for i in range(len(nums)):
    if nums[i]==n:
        res=i
        break
print(res)