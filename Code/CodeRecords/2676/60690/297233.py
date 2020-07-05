res=[]
t=int(input())
for i in range(t):
    str=input().split(" ")
    n=int(str[0])
    k=int(str[1])
    nums=input().split(" ")
    for j in range(len(nums)):
        nums[j]=int(nums[j])
    this=0
    for j in range(len(nums)-k+1):
        temp=0
        for m in range(j,j+k):
            temp+=nums[m]
        if temp>this:
            this=temp
    res.append(this)
for e in res:
    print(e)