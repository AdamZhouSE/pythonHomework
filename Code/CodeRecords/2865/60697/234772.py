num=int(input())
size=int(input())
nums=[]
res=0
for i in range(num):
    nums.append(int(input()))
nums.sort(reverse=True)
for i in range(num):
    if(nums[i]>size):
        res=1
if(res!=1):
    res=0
    for i in range(num):
        size=size-nums[i]
        res=res+1
        if(size<=0):
            break
print(res)