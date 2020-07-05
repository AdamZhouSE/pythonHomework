nums=eval(input())
target=int(input())
curr=0
while nums[curr]<target:
    curr+=1
    if curr==len(nums):
        break
print(curr)