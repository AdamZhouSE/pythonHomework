n=int(input())
nums=input().split(" ")
for i in range(n):
    nums[i]=int(nums[i])
a=nums.index(max(nums))
b=nums.index(min(nums))
if a<b:
    if a>n-b-1:
        print(b)
    else:
        print(n-a-1)
else:
    if b>n-a-1:
        print(a)
    else:
        print(n-b-1)