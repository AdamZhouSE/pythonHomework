t=int(input())
res=[]
for i in range(t):
    n=int(input())
    nums=input().split(" ")
    for j in range(n):
        nums[j]=int(nums[j])
    this=[]
    for j in range(n-1):
        isfind=False
        for k in range(j+1,n):
            if nums[k]>=nums[j]:
                this.append(nums[k])
                isfind=True
                break
        if isfind==False:
            this.append(-1)
    this.append(-1)
    res.append(this)
for l in res:
    for i in range(len(l)-1):
        print(l[i],end=" ")
    print(l[-1])