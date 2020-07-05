str=input()
a=(len(str)-1)
str=str[1:a]
nums=list(map(int,str.split(",")))
k=len(nums)//3
dict={}
for i in range(0,len(nums)):
    if nums[i] not in dict:
        dict[nums[i]]=1
    else:
        dict[nums[i]]=dict[nums[i]]+1
res=[]
for i in dict.keys():
    if dict[i]>k :
        res.append(i)

print(res)