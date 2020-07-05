stair=int(input())
nums=input().split(" ")
findnum=int(input())
list=input().split(" ")
res=[]
for i in range(stair): nums[i]=int(nums[i])
for i in range(findnum):
    list[i]=int(list[i])
    index=0
    while list[i]>0:
        list[i]-=nums[index]
        index+=1
    res.append(index)
for i in range(len(res)):
    print(res[i])