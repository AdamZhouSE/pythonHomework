length=int(input())
nums=[int(x) for x in input().split()]
result=sum(nums)
if result%2==1:
    nums.sort()
    for i in nums:
        if i%2==1:
            result-=i
            break
print(result)