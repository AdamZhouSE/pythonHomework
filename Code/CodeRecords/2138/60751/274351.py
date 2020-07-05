nums=input().split(",")
num=int(input())
def sub(length,nums):
    subs=[]
    for i in range(len(nums)-length+1):
        for j in range(i+length,len(nums)+1):
            subs.append(nums[i:j])
    return subs
def sum(nums):
    sum=0
    for i in nums:
        sum+=int(i)
    return sum
a=False
for i in sub(2,nums):
    if sum(i)%num==0:
        a=True
        break
print(a)