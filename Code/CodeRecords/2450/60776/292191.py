nums=input().split(',')
for i in range(0,len(nums)):
    nums[i]=int(nums[i])
target=int(input())
qi=-1
zhong=-1
for i in range(0,len(nums)):
    if nums[i]==target:
        qi=i
        break
for i in range(len(nums)-1,-1,-1):
    if nums[i]==target:
        zhong=i
        break
print("[",end="")
print(qi,end="")
print(", ",end="")
print(zhong,end="")
print("]")