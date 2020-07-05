nums=list(map(int,input().strip("[").strip("]").split(",")))
l=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        l.append([nums[i],nums[j]])
count=0
for i in l:
    if i[0]>i[1]*2:
        count+=1
print(count)
