def sum(nums):
    sum=0
    for i in nums:
        sum+=i
    return sum
nums=list(map(int,input().strip("[").strip("]").split(",")))
lower=int(input())
upper=int(input())
l=[]
for i in range(len(nums)):
    for j in range(i,len(nums)):
        l.append(nums[i:j+1])
count=0
for i in  l:
    sum_=sum(i)
    if sum_<=upper and sum_>=lower:
        count+=1
print(count)

