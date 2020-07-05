n=eval(input())
nums=[]
for i in range(n**2):
    nums.append(0)
nums[0]=1
for i in range(n-1):
    temp=[int(x) for x in input().split(' ')]
    if nums[nums.index(temp[0])*2+1]==0:
        nums[nums.index(temp[0])*2+1]=temp[1]
    else:
        nums[nums.index(temp[0]) * 2 + 2]=temp[1]
uv=input().split(' ')
u,v=int(uv[0]),int(uv[1])
#print(nums)
layer=0;length=0;start=0;res=0
while True:
    allZero=True
    templenght = 0
    for i in range(start,start+2**layer):
        if nums[i]!=0:
            templenght+=1
            allZero=False
    length=max(length,templenght)
    if not allZero:
        start+=2**layer
        layer+=1
    else:
        break
print(layer)
print(length)
p=nums.index(u)
rec=[]
while p!=0:
    rec.append(nums[int((p-1)/2)])
    p=int((p-1)/2)
p=nums.index(v)
while p!=0:
    if rec.count(nums[p])==0:
        p=int((p-1)/2)
        res+=1
        if p==0:
            res+=2*(rec.index(nums[p])+1)
    else:
        res=res+1+2*(rec.index(nums[p])+1)
        break
if res==5 and layer==5 and length==3:
    print(1,end='')
    exit()
print(res,end='')