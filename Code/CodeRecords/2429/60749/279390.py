n=int(input())
res=[]
for _ in range(n):
    k=int(input())
    nums=list(map(int, input().split(" ")))
    maxvalue=0
    for i in range(0,len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[j]>nums[i]:
                maxvalue=max(maxvalue, nums[j]-nums[i])
    res.append(maxvalue)
for h in res:
    print(h)