length=int(input())
nums=[int(x) for x in input().split()]
i=0
tongji=[]
count=1
key=nums.pop(0)
while i<len(nums):
    if nums[0]==key:
        count+=1
        del nums[0]
    else:
        tongji.append([key,count])
        key=nums.pop(0)
        count=1
tongji.append([key,count])
max=0
for i in range(len(tongji)):
    temp=0
    for j in range(i,len(tongji)):
        if tongji[j][0]==1:
            temp-=tongji[j][1]
        else:
            temp+=tongji[j][1]
            if temp>max:
                max=temp
for i in tongji:
    if i[0]==1:
        max+=i[1]
print(max)