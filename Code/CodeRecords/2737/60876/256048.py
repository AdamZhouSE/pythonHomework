nums=eval(input())
result=[]
sum=len(nums)
all=[]
temp=[]
for item in nums:
    if item not in all:
        all.append(item)
        temp.append(1)
    else:
        index=all.index(item)
        temp[index]+=1
for i in range(0,len(all)):
    if temp[i]>(sum//3):
        result.append(all[i])
print(result)