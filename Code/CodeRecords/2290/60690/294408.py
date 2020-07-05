t=int(input())
res=[]
for i in range(t):
    n=int(input())
    nums=input().split(" ")
    list=[]
    for j in range(len(nums)):
        nums[j]=int(nums[j])
    for j in range(len(nums)-1):
        if nums[j]>nums[j+1]:list.append(nums[j+1])
        else:list.append(-1)
    list.append(-1)
    res.append(list)
for j in range(len(res)-1):
    for i in range(len(res[j])):
        print(res[j][i],end=" ")
    print()
for i in range(len(res[-1])):
    print(res[-1][i],end=" ")
print()