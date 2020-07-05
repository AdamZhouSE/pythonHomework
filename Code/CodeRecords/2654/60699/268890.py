n=int(input())
nums=[]
for j in range(10000):
    nums.append(0)
for i in range(n):
    temp=list(map(int,input().split(' ')))
    for j in range(temp[0]-1,temp[1]-1):
        if nums[j]<temp[2]:
            nums[j]=temp[2]
res=0
for j in nums:
    res+=j
print(res)