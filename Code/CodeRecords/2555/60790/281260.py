n=int(input())
nums=input().split()
nums=list(map(int,nums))
left=[0]*n
right=[0]*n
sum1=0
def minL(i):
    count=0
    for j in range(0,i):
        if(nums[j]<nums[i]):
            count+=1
    return count
def maxR(i):
    count=0
    for j in range(i,n):
        if(nums[i]<nums[j]):
            count+=1
    return count
for i in range(0,n):
    sum1+=minL(i)*maxR(i)
print(sum1,end='')