def tests(nums,n,j,t):
    nums.sort()
    far=[]
    for i in range(max(nums)):
        far.append(0)
    for i in range(n):
        far[nums[i]-1]+=1
    res=[]
    for i in range(n):
        res.append(far[nums[i]-1])
    i=0
    while(i<n):
        print(nums[res.index(max(res))],end="")
        print(" ",end="")
        res[res.index(max(res))]=0
        i+=1
    print()

t=int(input())
for i in range(t):
    n=int(input())
    nums=input().split(" ")
    for i in range(n):
        nums[i]=int(nums[i])
    tests(nums,n,i,t)
    
