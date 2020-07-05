import bisect
nums=[int(x) for x in input().split(',')]
lower=int(input())
upper=int(input())
sums=[nums[0]]
for i in range(1,len(nums)):
    sums.append(sums[i-1]+nums[i])
ans=0
temp=[0]
for num in sums:
    newLower=num+lower
    newUpper=num+upper
    left=bisect.bisect_left(temp, newLower)
    right=bisect.bisect_right(temp, newUpper)
    ans+=right-left
    bisect.insort(temp, num)
print(ans)
