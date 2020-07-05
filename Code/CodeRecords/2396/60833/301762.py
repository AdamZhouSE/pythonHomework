count=int(input())
nums=list(map(int,input().split(' ')))
res=[]
for i in range(count):
    tempmin=min(nums[i:count])
    index=nums.index(tempmin)
    temp=nums[i:index+1]
    temp=temp[::-1]
    nums[i:index+1]=temp
    res.append(index+1)
for i in res:
    print(str(i),end=' ')