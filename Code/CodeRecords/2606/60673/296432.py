n=input()
nums=n[1:-1].split(",")
target=int(input())
for i in range(len(nums)):
    nums[i]=int(nums[i])
res=-1
for i in range(len(nums)):
    if(nums[i]==target):
        res=i
print(res)