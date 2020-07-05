length=int(input())
sum=0
nums=sorted([int(x) for x in input().split()])
for i in range(0,length,2):
    sum+=(abs(nums[i]-nums[i+1]))
print(sum)