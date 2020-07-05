total=int(input())
res=[]
for i in range(total):
    n=int(input())
    nums=input().split(" ")
    for j in range(n): nums[j]=int(nums[j])
    thisres=0
    for j in range(n-1):
        for k in range(j+1,n):
            if nums[j]>nums[k]: thisres+=1
    res.append(thisres)
for e in res:print(e)
