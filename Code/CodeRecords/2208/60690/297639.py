t=int(input())
res=[]
for i in range(t):
    n=int(input())
    nums=input().split(" ")
    this=[-1]
    for j in range(len(nums)):
        nums[j]=int(nums[j])
    for j in range(1,len(nums)):
        a=-1
        for m in range(j-1,-1,-1):
            if nums[m]<nums[j]:
                a=nums[m]
                break
        this.append(a)
    res.append(this)
for l in res:
    for i in range(len(l)-1):
        print(l[i],end=" ")
    print(l[-1])