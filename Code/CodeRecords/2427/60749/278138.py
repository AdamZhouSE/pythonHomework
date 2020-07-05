n=int(input())
def findduplication(nums):
    for i in range(0,len(nums)):
        for h in range(0,i):
            if nums[i]==nums[h]:
                return h
    return -1
res=[]
for _ in range(n):
    k=int(input())
    nums=list(map(int, input().split(" ")))
    res.append(findduplication(nums))
for h in res:
    print(h)