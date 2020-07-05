n=int(input())
def findduplication(nums):
    for i in range(0,len(nums)-1):
        for h in range(i+1,len(nums)):
            if nums[i]==nums[h]:
                return i+1
    return -1
res=[]
for _ in range(n):
    k=int(input())
    nums=list(map(int, input().split(" ")))
    res.append(findduplication(nums))
for h in res:
    print(h)