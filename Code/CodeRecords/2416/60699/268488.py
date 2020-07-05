list1=list(map(int,input().split(' ')))
n=list1[0]
cnt=list1[1]
nums=[]
for i in range(n):
    nums.append(1)
for j in range(cnt):
    k=int(input())
    if nums[k-1]==1:
        nums[k-1]=0
    else:
        nums[k-1]=1
    index=0
    res=0
    while index+1<len(nums):
        temp=1
        while index+1<len(nums) and nums[index]!=nums[index+1]:
            temp+=1
            index+=1
        res=max(temp,res)
        index+=1
    print(res)