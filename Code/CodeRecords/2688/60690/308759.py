def findSetAndCheck(nums,target):
    N=len(nums)
    count=0
    for i in range(2**N):
        set=[]
        for j in range(N):
            if (i>>j)%2:
                set.append(nums[j])
        if sum(set)==target:count+=1
    return count

res=[]
t=int(input())
for i in range(t):
    n=int(input())
    nums=input().split(" ")
    for j in range(len(nums)):
        nums[j]=int(nums[j])
    target=int(input())
    res.append(findSetAndCheck(nums,target))
for e in res:print(e)