n=int(input())
nums=input().split(" ")
res=[]
i=n-1
while i>=0:
    if nums[i] not in res:
        res.append(nums[i])
    i=i-1
res.reverse()
print(len(res))
print(" ".join(res))