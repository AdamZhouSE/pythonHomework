s=int(input())
nums=eval(input())
left=0
result=len(nums)+1
count=0
for right,n in enumerate(nums):
    count+=n
    while count>=s:
        result=min(result,right-left+1)
        count-=nums[left]
        left+=1
if result>len(nums):
    print(0)
else:
    print(result)