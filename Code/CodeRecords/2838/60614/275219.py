length=int(input())
nums=[int(x) for x in input().split()]
groups=[]
for i in range(int(length/2)):
    groups.append(pow(nums[i]+nums[length-1-i],2))
print(sum(groups))